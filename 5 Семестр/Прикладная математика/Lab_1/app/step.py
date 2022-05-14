import numpy as np


def step(tau, pPos):
    rowN, colN = tau.shape
    newTau = np.eye(rowN, colN)

    i, j = pPos
    pValue = tau[i][j]
    newTau[i] = tau[i] / pValue

    for eq_i, _ in enumerate(tau):
        if eq_i != i:
            multiplier = newTau[i] * tau[eq_i][j]
            newTau[eq_i] = tau[eq_i] - multiplier # TODO fix some bug

    return np.round(newTau, 5)