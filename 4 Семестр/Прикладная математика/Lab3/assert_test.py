import numpy as np
import scipy
from scipy.linalg import lu_solve
import lu_decomposition
import linear_equations_solving as les
import generate_matrix as gm
from parameters import *
from time import time
import testset as ts
from scipy.sparse import csr_matrix


def is_singular(matrix):
    return True if np.linalg.det(matrix) == 0 or np.linalg.cond(matrix) > 10 ** 16 else False


def test_plu(size=default_size, k=default_k, full_log=False):
    # A_matrix_list = gm.generate_list_of_matrix(gm.get_ak_matrix)
    # b_matrix_list = gm.generate_list_of_matrix(gm.simple_random_matrix)
    for i in ts.plu_decomposition:
        for j in ts.b:
            if is_singular(i):
                continue
            if full_log:
                print('Число обусловенности')
                print(np.linalg.cond(i))
                print('-------(A, b)--------')
                print(i, j)
                print('--------scipy--------')
                print(scipy.linalg.lu_factor(i))
                print('--------numpy--------')
                print(np.linalg.solve(i, j))
            lu_decomposition.get_plu_decomposition(csr_matrix(i))
            lu_decomposition.plu_solve_full(i, j)
            lu_decomposition.invert(i)


def run_seidel(A, b, full_log=False):
    if full_log:
        print('-' * 5 + 'A' + '-' * 5)
        print(A)
        print('-' * 5 + 'b' + '-' * 5)
        print(b)
    return les.seidel(A, b)


def test_seidel_ak(size=default_size, k=default_k, full_log=False):
    A_matrix_list = gm.generate_list_of_matrix(gm.get_ak_matrix, size, k)
    b_matrix_list = gm.generate_list_of_matrix(gm.simple_random_matrix, size)
    for i in A_matrix_list:
        for j in b_matrix_list:
            if is_singular(i.toarray()):
                continue

            run_seidel(i, j, full_log)


def test_seidel_hilbert(size=default_size, full_log=False):
    A_matrix_list = gm.generate_list_of_matrix(gm.get_hilbert, size)
    b_matrix_list = gm.generate_list_of_matrix(gm.simple_random_matrix, size)
    for i in A_matrix_list:
        for j in b_matrix_list:
            run_seidel(i, j, full_log)


def plu_bt(A_list, b_list):
    for A in A_list:
        # print("COND")
        # print(np.linalg.cond(A.A))
        # p, l, u = scipy.linalg.lu(A.A)
        # print('scipy')
        # print(p@l@u)
        P, L, U = lu_decomposition.get_plu_decomposition(A)
        # print('my plu')
        # print((P@L@U).A)
        for b in b_list:
            # print('x by numpy')
            # print(np.linalg.solve(A.A, b))
            lu_decomposition.plu_solve(P, L, U, b)


def seidel_bt(A_list, b_list, real_b):
    result = []
    for A in A_list:
        r = []
        for b in b_list:
            r.append(les.seidel(A, b, real_b)[1])
        result.append(r.copy())


def big_test():
    start = time()
    A_matrix_list = gm.generate_list_of_matrix(gm.get_hilbert, quantity=1)
    # A_ak_matrix_list = gm.generate_list_of_matrix(gm.get_ak_matrix, k=default_k)
    b_matrix_list = gm.generate_list_of_matrix(gm.simple_random_matrix)
    # single_b = gm.generate_list_of_matrix(gm.simple_matrix, quantity=1)
    # print(A_ak_matrix_list)
    single_b = [A_matrix_list[0].A@b_matrix_list[0]]

    print("Generating matrices done!")
    print(time() - start)

    start = time()
    # plu_bt(A_matrix_list, single_b)
    print("PLU decomposition with Hilbert matrix done!")
    print(time() - start)

    # start = time()
    # plu_bt(A_ak_matrix_list, single_b)
    # print("PLU decomposition done!")
    # print(time() - start)

    start = time()
    # seidel_bt(A_matrix_list, single_b, b_matrix_list[0])
    print("Seidel with Hilbert matrix done!")
    print(time() - start)

    # start = time()
    # seidel_bt(A_ak_matrix_list, single_b, b_matrix_list[0])
    # print("Seidel done!")
    # print(time() - start)

    lu_decomposition.invert(A_matrix_list[0])


# test_plu()
# test_seidel_ak(default_size, default_k)
# test_seidel_hilbert(default_size)
big_test()
# test_plu(full_log=True)
A = np.array([[1, 2, 3, 4],
     [5, 4, 2, 5],
     [2, 3, 1, 4],
     [5, 1, 5, 2]], dtype=np.double)
b = np.array(range(1, 5))

# run_seidel(csr_matrix(A), b)
# lu_decomposition.get_plu_decomposition(csr_matrix(A))