import csv
from termcolor import colored


def write_data_fo_file(data: list, filename="output.csv", head=6, tail=3, dots=True):
    with open(filename, "w") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        if head + tail >= len(data):
            csvWriter.writerows(data)
        else:
            csvWriter.writerows(data[0:head])
            if dots:
                csvWriter.writerows([["..."]*len(data[0])])
            csvWriter.writerows(data[len(data)-tail:])
    my_csv.close()


class DataItem:
    def __init__(self, a, b, epsilon, value):
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.value = value


def get_data():
    testData = []

    for line in open('./tests/tests_lab1.txt', 'r').readlines():
        a, b, eps, val = list(map(float, line.split()))
        testData.append(DataItem(a, b, eps, val))

    return testData


def run_tests(mathFunction):
    data = get_data()
    all_data, passed, failed = len(data), 0, 0

    print(colored('Function name: ' + mathFunction.__name__, 'white', attrs=['reverse', 'blink']))

    for item in data:
        functionResult = mathFunction(item.a, item.b, item.epsilon)

        if abs(item.value - functionResult) > item.epsilon:
            color = 'red'
            state = 'TEST FAILED'
            failed += 1
        else:
            color = 'green'
            state = 'TEST PASSED'
            passed += 1

        print(colored(state + ':', color, attrs=['reverse', 'blink']) + ' ' + colored(
            'a: ' + str(item.a) + '  b: ' + str(item.b) + '  expected: ' + str(item.value) + '  got: ' + str(
                functionResult), 'white', attrs=['blink']))

    print(colored('Overview:', 'white', attrs=['reverse', 'blink']) + colored(' All: ' + str(all_data), 'white',
                                                                              attrs=['bold', 'blink']) + colored(
        ' Passed: ' + str(passed), 'green', attrs=['bold', 'blink']) + colored(' Failed: ' + str(failed), 'red',
                                                                               attrs=['bold', 'blink']))