from numpy.linalg import norm, inv, det
from functools import reduce
from random import random
import math
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from tools import write_data_fo_file

n = 1000
s = (n, n)
A = np.zeros(s)
condition_number = 0


def generate_matrix(n: int):
    s = (n, n)
    Y = np.zeros(s)

    for i in range(0, n):
        for j in range(i, n):
            Y[i][i] = random()
            A[i][i] = Y[i][i]
    return Y


def generate_func(n: int):
    def line_mapper(line, line_number, *args):
        return reduce(lambda prev, cur: prev + args[line_number] * args[cur[0]] * cur[1], enumerate(line), 0)

    matrix = generate_matrix(n)
    print(reduce(lambda prev, line: prev + ' '.join(map(lambda v: '%.3f' % v, line)) + '\n', matrix, ''), end='')
    get_f(matrix, n)
    print("Condition number:", np.linalg.cond(matrix))
    return lambda *args: reduce(lambda val, line: val + line_mapper(line[1], line[0], *args), enumerate(matrix),
                                0), np.linalg.cond(matrix)


def get_f(S, n):
    string = ' '
    for i in range(n):
        string += str(S[i, i]) + '*x[' + str(i) + ']**2'
        if (i != n - 1):
            string += ' + '
    print(str(string))
    return string

def function(x):
    y = [0] * len(x)
    for i in range(len(x)):
        y[i] = x[i] ** 2 * A[i][i]
    return sum(y)


def gradfunction(x):
    y = [0] * len(x)
    for i in range(len(x)):
        y[i] = x[i] * A[i][i]
    return y





def ConstStep():
    x = [0] * n
    for i in range(n):
        x[i] = 1
    epsilon = 0.01
    steps = 1e-1
    count = 0
    while 1:
        grad = gradfunction(x)
        count += 1

        if norm(grad) < epsilon:
            print("Count of steps: " + str(count))
            return count
        if count > 1000000 / steps:
            for i in range(0, len(x) - 1):
                x[i] = 9e10
            return x
        alpha = steps
        for i in range(n):
            x[i] = x[i] - alpha * grad[i]


# F,condition_number=generate_func(10)
# ConstStep()

x_res = []
y_res = []
for i in range(100):
    F, condition_number = generate_func(2)
    x_res.append(condition_number)
    y_res.append(ConstStep())
print(x_res, y_res)
points = []
points_srt = []
for i in range(len(x_res)):
    if x_res[i] <= 10:
        points.append((x_res[i], y_res[i]))
points_srt = sorted(points, key=lambda point: point[0])

for i in range(len(points_srt)):
    x_res[i] = points_srt[i][0]
    y_res[i] = points_srt[i][1]
print(x_res)
plt.axis((0, 10, 0, 300))

plt.plot(x_res, y_res, 'ro', label='n = 2')

x_res1 = []
y_res1 = []
for i in range(100):
    F, condition_number = generate_func(5)
    x_res1.append(condition_number)
    y_res1.append(ConstStep())
print(x_res1, y_res1)
points = []
points_srt = []

for i in range(len(x_res1)):
    if x_res1[i] <= 10:
        points.append((x_res1[i], y_res1[i]))
points_srt = sorted(points, key=lambda point: point[0])

for i in range(len(points_srt)):
    x_res1[i] = points_srt[i][0]
    y_res1[i] = points_srt[i][1]

gp = plt.plot(x_res1, y_res1, 'go', label='n = 5')

x_res1 = []
y_res1 = []
for i in range(100):
    F, condition_number = generate_func(10)
    x_res1.append(condition_number)
    y_res1.append(ConstStep())
print(x_res1, y_res1)
points = []
points_srt = []

for i in range(len(x_res1)):
    if x_res1[i] <= 10:
        points.append((x_res1[i], y_res1[i]))
points_srt = sorted(points, key=lambda point: point[0])

for i in range(len(points_srt)):
    x_res1[i] = points_srt[i][0]
    y_res1[i] = points_srt[i][1]

bp = plt.plot(x_res1, y_res1, 'bo', label='n = 10')
plt.legend()
plt.xlabel('k')
plt.ylabel('iteration count')

plt.show()
