import numpy as np

from app.isBasic import is_basic

def solve(tau):
    columns = np.array(tau).T
    solutions = []

    for column in columns[:-1]:
        solution = 0
        if is_basic(column):
            index = column.tolist().index(1)
            solution = columns[-1][index]
        solutions.append(solution)
    return solutions, tau[-1][-1] * -1