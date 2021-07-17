import math

import function as f
import numpy as np
import pandas as pd
eps = 0.0001


def newton(y, x):
    saved_x = []
    saved_y = []
    steps = -1

    while 1:
        grad = f.grad(y, x)

        steps += 1
        saved_x.append(x[0])
        saved_y.append(x[1])
        if steps > 1000000:
            print("Сломался Newton")
            return
        if np.linalg.norm(grad) <= eps:
            df = pd.DataFrame({'X': saved_x, 'Y': saved_y})
            return {
                'x': x,
                'points': df,
                'steps': steps,
                'logs': [[i, saved_x[i], saved_y[i]] for i in range(steps+1)]
            }
        x = x - np.dot(np.linalg.inv(H(x)), grad)


# def H():
#     arr = [[2, 1], [1, 2]]
#     return np.array(arr)

def H(x):
    arr = [[1/2-math.sin(x[0]), 0], [0, 1/2]]
    return np.array(arr)
