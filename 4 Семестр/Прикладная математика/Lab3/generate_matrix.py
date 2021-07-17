import scipy.sparse as sps
from scipy.sparse import csr_matrix
import numpy as np
from random import choice
import warnings
from parameters import *

warnings.filterwarnings("ignore", message="Changing the sparsity structure of a csr_matrix is expensive.")
np.set_printoptions(suppress=True)


def is_singular(matrix):
    return True if np.linalg.cond(matrix) > 10 ** 16 else False


# def get_hilbert(size=default_size):
#     matrix = sps.rand(size, size, density=0.0, format='csr', dtype=np.float64)
#     for i in range(size):
#         for j in range(size):
#             print(i, j)
#             matrix[i, j] = 1.0 / (i + j + 1.0)
#     if is_singular(matrix.A):
#         return get_hilbert(size)
#     return matrix

def get_hilbert(size=default_size):
    v = np.arange(1, size + 1) + np.arange(0, size)[:, np.newaxis]
    return csr_matrix(1. / v)


def get_ak_matrix(size=default_size, k=default_k):
    singular = True

    while singular:
        matrix = sps.rand(size, size, density=0.80, format='lil', dtype=np.double)
        numbers = [0, -1, -2, -3, -4]
        for i in range(size):
            for j in range(size):
                if i == j:
                    continue
                randNum = choice(numbers)
                if randNum == 0:
                    continue
                matrix[i, j] += randNum + 10 ** (-k)
        for i in range(size):
            summ = 0
            for j in range(size):
                if i == j:
                    continue
                summ += matrix[i, j]
            matrix[i, i] = summ
        singular = is_singular(matrix.A)
        print(1)
    return csr_matrix(matrix)


def simple_random_matrix(size=default_size):
    return np.random.randint(1, 100, size=size)


def simple_matrix(size=default_size):
    return np.array(range(1, size + 1))


# Generate list of matrices by given function and parameters
def generate_list_of_matrix(generator, size=default_size, quantity=default_quantity, k=None):
    if k is None:
        return np.array([generator(size) for _ in range(quantity)])
    else:
        return np.array([generator(size, k) for _ in range(quantity)])
