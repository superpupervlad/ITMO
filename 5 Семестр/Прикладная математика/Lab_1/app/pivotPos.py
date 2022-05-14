import numpy as np
import math

def pivotPos(tau, is_max):
    z = tau[-1][:-1] if not is_max else np.negative(tau[-1][:-1])

    column = np.argmin(z)

    bounds = []

    for eq in tau[:-1]:
        el = eq[column]
        bounds.append(math.inf if el <= 0 else eq[-1] / el)

    if all([r == math.inf for r in bounds]):
        raise Exception("Решения нет")

    row = np.argmin(bounds)
    return row, column