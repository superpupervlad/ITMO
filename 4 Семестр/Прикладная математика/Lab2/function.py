import math

import numpy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

eps = 1e-8
l = 0.01

ratio = (1 + math.sqrt(5)) / 2

# 1 функция
# def function(x):
#     return (x[0] - 2) ** 2 + x[0] * x[1] + (x[1] + 1) ** 2


# 2 функция
def function(x):
    return x[0]**2/4 + x[1]**2/4 + numpy.sin(x[0])


# def gradient(y, x, i):
#     x[i] = x[i] + eps
#     a = eval(y)
#     x[i] = x[i] - 2 * eps
#     b = eval(y)
#     return (a - b) / (2 * eps)


# def grad(y, x):
#     arr = []
#     for i in range(len(x)):
#         x[i] = x[i] + eps
#         a = eval(y)
#         x[i] = x[i] - 2 * eps
#         b = eval(y)
#         x[i] = x[i] +  eps
#         arr.append((a - b) / (2 * eps))
#     return np.array(arr)

# def grad(y, x):
#     arr = [2 * (x[0] - 2) + x[1], x[0] + 2 * (x[1]+1)]
#     return np.array(arr)


def grad(y, x):
    arr = [x[0] / 2 + math.cos(x[0]), x[1] / 2]
    return np.array(arr)


def make_3d_graph():
    graph_begin = -15
    graph_end = 15
    precision = 0.05

    fig = plt.figure(figsize=(10, 10))
    ax = fig.gca(projection="3d")

    X = np.arange(graph_begin, graph_end, precision)
    Y = np.arange(graph_begin, graph_end, precision)

    xmesh, ymesh = np.meshgrid(X, Y)
    ax.plot_surface(xmesh, ymesh, function([xmesh, ymesh]), cmap=cm.plasma)

    plt.xlabel('X', fontsize=15)
    plt.ylabel('Y', fontsize=15)
    ax.set_zlabel('f(X, Y)', fontsize=15)

    plt.show()


def make_2d_graph(data, title=""):
    graph_begin = -15
    graph_end = 15
    precision = 100  # curveness of counter lines
    label_size = 17
    max_lines = 30

    x_res = data.tail(1)['X'].values[0]
    y_res = data.tail(1)['Y'].values[0]

    for i in range(len(data['X'])):
        if data['X'][i] > graph_end:
            data['X'][i] = graph_end
        if data['X'][i] < graph_begin:
            data['X'][i] = graph_begin

    for i in range(len(data['Y'])):
        if data['Y'][i] > graph_end:
            data['Y'][i] = graph_end
        if data['Y'][i] < graph_begin:
            data['Y'][i] = graph_begin

    X, Y = np.meshgrid(np.linspace(graph_begin, graph_end, precision),
                       np.linspace(graph_begin, graph_end, precision))
    Z = function([X, Y])
    plt.plot(np.array(data['X']), np.array(data['Y']), marker='o')
    plt.plot(x_res, y_res, 'x', markersize=10, color='red', marker='*')
    plt.contour(X, Y, Z, max_lines)
    plt.xlabel("X", size=label_size)
    plt.ylabel("Y", size=label_size)
    plt.title(title, size=label_size)
    print(x_res, y_res)
    plt.show()
