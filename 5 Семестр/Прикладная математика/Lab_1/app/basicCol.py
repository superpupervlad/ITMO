import numpy as np
import itertools

from app.isBasic import is_basic
from app.step import step

def basicCol(tau):
    columns = np.array(tau).T

    rowsIdx = list(range(len(columns[0]) - 1))
    colIdx = list(range(len(columns) - 1))

    count = 0

    for _, col in enumerate(columns[:-1]):
        if is_basic(col):
            count = count + 1

            rowsIdx.remove(np.argmax(col))
            colIdx.remove(np.argmax(colIdx))

    for _ in range(len(columns[0]) - 1 - count):
        el_iter = itertools.product(rowsIdx, colIdx)
        idx = next(el_iter)

        while tau[idx[0]][idx[1]] == 0:
            idx = next(el_iter)

        tau = step(tau, (idx[0], idx[1]))

        rowsIdx.remove(idx[0])
        colIdx.remove(idx[1])

    return tau
