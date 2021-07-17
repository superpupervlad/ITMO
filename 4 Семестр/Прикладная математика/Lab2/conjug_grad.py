import function as f
import numpy as np
import math
import pandas as pd
import one

ratio = (1 + math.sqrt(5)) / 2
eps = 0.0001


def conjug_grad(funcStr, x):
    saved_x = [x[0]]
    saved_y = [x[1]]
    steps = 0
    while 1:
        p = - f.grad(funcStr, x)
        grad = p
        while 1:
            steps += 1
            alpha = one.fibonachi(lambda al: f.function(x + al * p))
            x = x + alpha * p
            grad1 = -f.grad(funcStr, x)

            if steps % 2 == 0:
                B = 0
            else:
                B = (np.dot(grad1, grad1)) / (np.dot(grad, grad))

            p = grad1 + B * p
            grad = grad1.copy()
            saved_x.append(x[0])
            saved_y.append(x[1])
            if np.dot(grad, grad) < eps:
                df = pd.DataFrame({'X': saved_x, 'Y': saved_y})

                return {
                    'x': x,
                    'points': df,
                    'steps': steps,
                    'logs': [[i, saved_x[i], saved_y[i]] for i in range(steps+1)]
                }
