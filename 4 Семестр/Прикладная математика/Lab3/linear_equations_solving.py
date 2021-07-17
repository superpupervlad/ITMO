import numpy as np
import numpy.linalg

from parameters import *
from tools import write_data_fo_file


def seidel(A, b, real_b):
    n = A.get_shape()[0]
    x = np.zeros(n)

    converge = False
    count = 0
    # print("A")
    # print(A.A)
    # print("b")
    # print(b)

    r = [count]
    r.extend(x.tolist())
    data = [r]
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A.A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A.A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A.A[i][i]
        count += 1

        print(np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))))
        converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= default_eps
        x = x_new
        # r = [count]
        # r.extend(x.tolist())
        # data.append(r)

    # write_data_fo_file(data)

    # npx = numpy.linalg.solve(A, b)
    a = 0
    # for i in range(len(x)):
    #     a += abs(real_b[i] - x[i]) * 100

    print('AAAAAAAAAAAAAAAAAAA')
    print(a/len(x))

    # print('_____________ЗЕЙДЕЛЬ________________')
    # print('Матрица A')
    # print(A)
    # print('Наш x')
    # print(x)
    # print('Полученное значение b при умножении А на наш x')
    # print(A@x)
    # print('x by numpy')
    # print(numpy.linalg.solve(A, b))
    # print('Изначальное значение b')
    # print(b)
    print('COUNT')
    print(count)
    # assert (np.allclose(A@x, b, atol=default_eps))

    return x, count
