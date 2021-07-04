import re
import jenkins
from bokeh.plotting import figure, show, output_file
from bokeh.models import Span, ResetTool, WheelZoomTool, PanTool, HoverTool, ColumnDataSource, FixedTicker
import itertools
from bokeh.palettes import Magma5 as palette  # Вот здесь можно поиграться с цветами
colors = itertools.cycle(palette)


# Настройки подключения
jenkins_domain = ""  # http://1.2.3.4:5678
jenkins_username = ""
jenkins_password = ""
# Настройки инфы о лабах
nickname = "vlad"
lab = 1
jenkins_job = f"{nickname}-lab{lab}"
normal_total_tests = [35, 68, 159, 200][lab - 1]
# Настройки графика
max_width = 1750
max_height = 800
sizing_mode = "stretch_both"  # https://docs.bokeh.org/en/latest/docs/reference/layouts.html#bokeh.layouts.Spacer.sizing_mode
minors_line_width = 2
majors_line_width = 3
show_circles = False
circles_size = 3
circles_color = "black"
output_file(jenkins_job + ".html")
# Пример: "brave"
# Возможно нужно будет в конец добавить %s, чтобы получилось "brave %s"
# В крайнем случае bokeh должен написать имя созданного .html файла, который нужно будет открыть вручную
browser = "CHANGE ME"


def download_data():
    server = jenkins.Jenkins(jenkins_domain, username=jenkins_username, password=jenkins_password)
    example_job_info = server.get_job_info(jenkins_job)
    number_of_builds = example_job_info['nextBuildNumber']
    build_console_logs = []
    print("Скачивание билд логов")
    for i in range(1, number_of_builds):
        print(f'\r{i}/{number_of_builds - 1}', end='')
        build_console_logs.append(server.get_build_console_output(jenkins_job, i))
    print()
    return [number_of_builds, build_console_logs]


def prepare_data(number_of_builds, raw_data):
    prepared_data = {
        "Total tests": [],
        "Failed": [],
        "Errors": [],
        "Failed + errors": [],
        "Commit_messages": []
    }
    for console_log in raw_data:
        try:
            prepared_data["Commit_messages"].append(re.search('Commit message: "(.+?)"', console_log).group(1))
        except IndexError:
            prepared_data["Commit_messages"].append('---')

        try:
            line_with_stats = console_log.split('Tests run')[1].split('\n')[0]
        except IndexError:
            line_with_stats = "0 0 0 0"

        stats = list(map(int, re.findall("\d+", line_with_stats)))
        if stats[0] != 0:
            prepared_data["Total tests"].append(stats[0])
            prepared_data["Failed"].append(stats[1])
            prepared_data["Errors"].append(stats[2])
            prepared_data["Failed + errors"].append(stats[1] + stats[2])
        else:
            for i in prepared_data:
                if i == "Commit_messages":
                    continue
                prepared_data[i].append('nan')

    prepared_data["y values"] = list(range(1, number_of_builds))
    return prepared_data


def make_plot(data):
    p = figure(
        tools=[PanTool(), ResetTool(), WheelZoomTool(), HoverTool(tooltips=[("Commit message", "@Commit_messages")])],
        sizing_mode=sizing_mode,
        max_width=max_width,
        max_height=max_height,)
    p.xaxis.ticker = FixedTicker(ticks=data["y values"])

    p.xaxis.axis_label = "Попытки"
    p.yaxis.axis_label = "Тесты"

    p.xaxis.axis_label_text_font_size = '23px'
    p.yaxis.axis_label_text_font_size = '23px'

    p.xgrid.grid_line_dash = [6, 4]
    p.ygrid.grid_line_dash = [6, 4]

    # Линия y=0 и линия нормального количества тестов
    normal_total_tests_line = Span(location=normal_total_tests, dimension="width", line_dash="dashed", line_width=minors_line_width)
    zero_line = Span(location=0, dimension="width", line_dash="dashed", line_width=minors_line_width)
    p.add_layout(normal_total_tests_line)
    p.add_layout(zero_line)

    source = ColumnDataSource(data)

    for category_name, category_data in data.items():
        if category_name in ("Commit_messages", "y values"):
            continue
        p.line("y values", category_name, source=source, legend_label=category_name, line_color=next(colors), line_width=majors_line_width)
        if show_circles:
            p.circle("y values", category_name, source=source, legend_label=category_name, color=circles_color, size=circles_size)

    show(p, browser=browser)


jenkins_data = download_data()
data_for_plot = prepare_data(jenkins_data[0], jenkins_data[1])
make_plot(data_for_plot)