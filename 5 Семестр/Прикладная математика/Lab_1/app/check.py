import numpy as np

from app.step import step


def check(tau):
    b = np.array(tau).T[-1][:-1]

    if any(x < 0 for x in b):
        row_id = np.argmin(b)
        col_id = np.argmin((tau[row_id][:-1]))
        tau = step(tau, (row_id, col_id))
    return tau