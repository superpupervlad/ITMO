import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


P_start = 10
P_min = 0
P_max = 50
start = -np.sqrt(10)
end = start * -1
density = 1000
values = np.linspace(start, end, density)
cos_color = "blue"
steps_color = "red"
fontsize = 16


def S(alpha, a, P):
    return np.cos(alpha*a) + P*np.sin(alpha*a) / (alpha*a)


def plot_cos(P, is_left=False):
    if is_left:
        mul = -1
    else:
        mul = 1

    return plt.plot(values * (mul * values), S(values, values, P), color=cos_color)


def plot_cos_sym(P):
    l1, = plot_cos(P)
    l2, = plot_cos(P, True)
    return [l1, l2]


def plot_bars(P, is_left=False):
    if is_left:
        mul = -1
    else:
        mul = 1

    return plt.plot(values * (mul * values), [1 if abs(S(i, i, P)) < 1 else 0 for i in values], color=steps_color)


def plot_bars_sym(P):
    l1, = plot_bars(P)
    l2, = plot_bars(P, True)
    return [l1, l2]


def plot_all(P):
    res = [plot_cos_sym(P), plot_bars_sym(P)]
    return res


def update(slider_val):
    bars_values = [1 if abs(S(i, i, slider_val)) < 1 else 0 for i in values]
    txt.set_text(f"{bars_values.count(0)/len(bars_values) * 100:.2f}" + "%")

    for p in lines[0]:
        p.set_ydata(S(values, values, slider_val))

    for p in lines[1]:
        p.set_ydata(bars_values)

    fig.canvas.draw_idle()


fig, ax = plt.subplots()

ax.set_xlabel('αa', fontsize=fontsize)
ax.set_ylabel('S(α,a)', fontsize=fontsize)


plt.axhline(y=1, linestyle="--")
plt.axhline(y=-1, linestyle="--")

lines = plot_all(P_start)
plt.text(10, 10.3, "Процент запрещенных зон", horizontalalignment='right', verticalalignment='top')
txt = plt.text(10, 10, "", horizontalalignment='right', verticalalignment='top')

plt.subplots_adjust(left=0.25)
ax_p = plt.axes([0.1, 0.25, 0.0225, 0.6])
p_slider = Slider(
    ax=ax_p,
    label="P",
    valmin=P_min,
    valmax=P_max,
    valinit=P_start,
    orientation="vertical"
)

p_slider.on_changed(update)

plt.show()
