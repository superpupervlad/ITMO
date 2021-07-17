import numpy as np
from scipy.sparse import csr_matrix
import warnings
from parameters import *

warnings.filterwarnings("ignore", message="Changing the sparsity structure of a csr_matrix is expensive.")
np.set_printoptions(suppress=True)


def get_plu_decomposition(A: csr_matrix):
    """
    Возращает PLU-разложение матрицы A, где
    A -- А изначальная матрица
        A = PLU
    P -- матрица перестановки
    L(Lower) -- нижняя матрица
    U(Upper) -- верхняя матрица

    Example: get_lu_decomposition(
                np.array([[0, 0, 26, 10],
                        [60, 0, 75, 0],
                        [0, 0, 0, 100],
                        [30, 0, 10, 0]], dtype='float'))

    Return: P, L, U
    P (csr_matrix): [[0. 1. 0. 0.]
                     [1. 0. 0. 0.]
                     [0. 0. 0. 1.]
                     [0. 0. 1. 0.]]

    L (csr_matrix): [[1.  0. 0. 0.]
                     [0.  1. 0. 0.]
                     [0.5 0. 1. 0.]
                     [0.  0. 0. 1.]]

    U (csr_matrix):  [[ 60. 0. 75.   0.  ]
                      [  0. 0. 26.   10. ]
                      [  0. 0. -27.5 0.  ]
                      [  0. 0. 0.    100.]]
    """

    n = A.toarray().shape[0]
    U = A.copy()
    L = csr_matrix(np.zeros_like(A.toarray()))
    P = csr_matrix(np.eye(n, dtype=np.double))

    for i in range(n - 1):
        index = np.argmax(abs(U[i:, i]))
        # "not U[i:, i][index] != 0" вместо "U[i:, i][index] == 0" потому что так быстрее
        if not U[i:, i][index] != 0:
            continue
        index += i
        if index != i:
            U[[index, i]] = U[[i, index]]
            P[[index, i]] = P[[i, index]]
            L[[index, i]] = L[[i, index]]
        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] -= factor * U[i]

    L += csr_matrix(np.eye(n, dtype=np.double))
    P = P.transpose()

    # assert (np.allclose(A, P@L@U, atol=default_eps))
    # print("A")
    # print(A.A)
    # print("P")
    # print(P.A)
    # print("L")
    # print(L.A)
    # print("U")
    # print(U.A)
    return P, L, U


def forward_substitution(L, b):
    # if np.isclose(np.linalg.det(L.toarray()), 0):
    #     warnings.warn("Matrix is singular!")

    n = L.shape[0]

    y = np.zeros_like(b, dtype=np.double)

    y[0] = b[0] / L[0, 0]
    for i in range(1, n):
        y[i] = (b[i] - L[i, :i]@y[:i]) / L[i, i]

    return y


def back_substitution(U, y):
    # if np.isclose(np.linalg.det(U.toarray()), 0):
    #     warnings.warn("Matrix is singular!")

    n = U.shape[0]

    x = np.zeros_like(y, dtype=np.double)

    x[-1] = y[-1] / U[-1, -1]
    # С конца в начало
    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - U[i, i:]@x[i:]) / U[i, i]

    return x


def plu_solve_full(A, b):
    P, L, U = get_plu_decomposition(A)
    y = forward_substitution(L, P.transpose()@b)
    x = back_substitution(U, y)

    assert (np.allclose(A@x, b, atol=default_eps))

    return x


def plu_solve(P, L, U, b):
    y = forward_substitution(L, P.transpose() @ b)
    x = back_substitution(U, y)
    # print('_____________LU Разложение_________________')
    # print('Матрица A')
    # print(P@L@U.A)
    # print('Наш x')
    # print(x)
    # print('Полученное значение b при умножении А на наш x')
    # print(P@L@U@x)
    # print('x by numpy')
    # print(np.linalg.solve(P@L@U.A, b))
    # print('Изначальное значение b')
    # print(b)
    # print('________________________________________')
    # npx = np.linalg.solve(P@L@U, b)
    a = 0
    # for i in range(len(x)):
    #     a += abs(npx[i] - x[i]) * 100

    print('AAAAAAAAAAAAAAAAAAA')
    print(a/len(x))
    assert (np.allclose((P@L@U) @ x, b, atol=default_eps))

    return x


def invert(A):
    print('A')
    print(A.A)
    inv = plu_solve_full(A, np.eye(A.shape[0]))

    assert (np.allclose(A@inv, np.eye(A.shape[0]), atol=default_eps))
    print('Inverse A')
    print(inv)
    print('A * A-1')
    print(A.A@inv)
    return inv