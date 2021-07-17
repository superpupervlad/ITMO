import pandas as pd
import function as f
import numpy as np

eps = 0.0001


def grad_crash(y, x):
    saved_x = [x[0]]
    saved_y = [x[1]]
    inner_x = x.copy()
    l = 1.0
    lastf = f.function(inner_x)
    steps = 0
    while l > 0.005:
        grad = f.grad(y, inner_x)
        gradx = f.grad(y, inner_x)[0]
        grady = f.grad(y, inner_x)[1]
        newx = inner_x[0] - l * gradx
        newy = inner_x[1] - l * grady
        newf = f.function([newx, newy])

        if np.linalg.norm(grad) <= eps:
            steps += 1
            saved_x.append(inner_x[0])
            saved_y.append(inner_x[1])
            df = pd.DataFrame({'X': saved_x, 'Y': saved_y})
            return {
                'x': inner_x,
                'points': df,
                'steps': steps,
                'logs': [[i, saved_x[i], saved_y[i]] for i in range(steps)]
            }

        if newf <= (lastf - 0.5 * l * (gradx * gradx + grady * grady)):
            inner_x[0] = newx
            inner_x[1] = newy
            lastf = newf
            steps += 1
            saved_x.append(inner_x[0])
            saved_y.append(inner_x[1])
        else:
            l = l * 0.5

