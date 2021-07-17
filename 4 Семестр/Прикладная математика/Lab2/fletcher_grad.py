import pandas as pd
import function as f
import numpy as np
import one

eps = 0.0001


def fletcher_grad(y, x):
    saved_x = [x[0]]
    saved_y = [x[1]]
    steps = 0
    k = 0

    while 1:
        N = 10
        p = - f.grad(y, x)

        while 1:
            alpha = one.fibonachi(lambda al: f.function(x + al * p))

            xk = x
            x = xk + alpha * p

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
                    'logs': [[i, saved_x[i], saved_y[i]] for i in range(steps+1)]
                }

            if k + 1 == N:
                k = 0
                break
            B = ((np.linalg.norm(funcGrad)) ** 2) / ((np.linalg.norm(funcGrad)) ** 2)
            pk = p
            p = - funcGrad + B * pk
            k += 1
