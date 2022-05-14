import numpy as np

def forceImprove(tau, is_max):
    z = tau[-1][:-1] if not is_max else np.negative(tau[-1][:-1])

    return any(x < 0 for x in z)