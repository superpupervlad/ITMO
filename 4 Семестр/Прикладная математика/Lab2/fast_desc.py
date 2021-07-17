import function as f
import pandas as pd
import numpy as np
import one

eps = 0.0001


def fast_desc(y, x):
    saved_x = []
    saved_y = []
    steps = -1

    while 1:
        funcGrad = f.grad(y, x)
        steps += 1
        saved_x.append(x[0])
        saved_y.append(x[1])
        if np.linalg.norm(funcGrad) < eps:
            df = pd.DataFrame({'X': saved_x, 'Y': saved_y})
            return {
                'x': x,
                'points': df,
                'steps': steps,
                'logs': [[i, saved_x[i], saved_y[i]] for i in range(steps)]
            }

        k = one.fibonachi(lambda q: f.function(x - q * funcGrad))
        x = x - k * funcGrad
