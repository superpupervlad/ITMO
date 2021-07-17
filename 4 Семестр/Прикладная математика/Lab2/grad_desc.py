import pandas as pd
import function as f
import numpy as np

l = 0.001
eps = 0.0001


def grad_desc(y, x):
    saved_x = []
    saved_y = []
    steps = -1

    while 1:
        grad = f.grad(y, x)

        steps += 1
        saved_x.append(x[0])
        saved_y.append(x[1])
        if np.linalg.norm(grad) <= eps:
            df = pd.DataFrame({'X': saved_x, 'Y': saved_y})
            return {
                'x': x,
                'points': df,
                'steps': steps,
                'logs': [[i, saved_x[i], saved_y[i]] for i in range(steps+1)]
            }

        x = x - l * grad
