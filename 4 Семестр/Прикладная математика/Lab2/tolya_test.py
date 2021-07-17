import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.linalg import norm
from matplotlib import cm


def obj_fun(x_):
    return 4 * x_[0] ** 2 + x_[1] ** 2 - x_[0] + 2 * x_[1]


def der_fun(x_):
    return np.array([2 * 4 * x_[0] - 1,
                     2 * x_[1] + 2])


fig = plt.figure(figsize=(10, 10))
ax = fig.gca(projection="3d")
X = np.arange(-2, 2, 0.05)
Y = np.arange(-2, 2, 0.05)
xmesh, ymesh = np.meshgrid(X, Y)
ax.plot_surface(xmesh, ymesh, obj_fun([xmesh, ymesh]), cmap=cm.plasma)
ax.view_init(elev=30, azim=120)
plt.xlabel('X', fontsize=15)
plt.ylabel('Y', fontsize=15)
ax.set_zlabel('f(X, Y)', fontsize=15)
plt.title("Objective function")
plt.show()


def constStep(start: np.array, eps: float, st: float):
    x1 = np.array(start)
    y1 = x1
    step_count = 0
    grad = - der_fun(x1)
    saved_x = [y1[0]]
    saved_y = [y1[1]]
    direct = [grad]
    while norm(der_fun(y1)) > eps:
        grad = - der_fun(y1)
        alpha = st
        y2 = y1 + alpha * grad
        y1 = y2
        step_count += 1
        saved_x.append(y1[0])
        saved_y.append(y1[1])
        direct.append(grad)
    print(step_count)
    df = pd.DataFrame({'X': saved_x, 'Y': saved_y, 'Directions': direct})
    return df


begin = (1, 1)
DFP = constStep(begin, 0.1, 0.1)
fig = plt.figure(figsize=(15, 15))
x = DFP['X']
y = DFP['Y']
for idx, row in DFP.iterrows():
    last_idx = DFP.iloc[-1].name
    if last_idx == idx:
        x = row[0]
        y = row[1]
X, Y = np.meshgrid(np.linspace(-1, 1.1, 31), np.linspace(-6, 4, 31))
Z = obj_fun([X, Y])
plt.plot(np.array(DFP['X']), np.array(DFP['Y']), marker='o', markersize=5)
plt.plot([1], [1], 'x', mew=1, markersize=10, color='green', marker='^')
plt.plot([x], [y], 'x', mew=1, markersize=10, color='red', marker='*')
plt.contour(X, Y, Z, np.logspace(-1, 1, 31))
plt.xlabel("X", fontsize=15)
plt.ylabel("Y", fontsize=15)
plt.show()