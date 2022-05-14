import numpy as np

def makeTau(c, A, b):
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]

    return np.array(xb + [z])
