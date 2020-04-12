#  1. Можно использовать Дейкстру из предыдущего задания
from sys import setrecursionlimit, maxsize
import threading
import array

setrecursionlimit(10 ** 9)
threading.stack_size(260000000)


def main():
    fin = open("pathsg.in")
    fout = open("pathsg.out", "w")
    inf = maxsize
    n, m = list(map(int, fin.readline().split()))
    matrix = [[inf] * n for _ in range(n)]

    for i in range(m):
        a, b, cost = (list(map(int, fin.readline().split())))
        matrix[a - 1][b - 1] = cost

    for l in range(n):
        not_visited = array.array('b', [1] * n)
        distance = [inf] * n
        distance[l] = 0
        for i in range(n):
            min_weight = maxsize
            index_min_weight = None
            for j in range(n):
                if not_visited[j] and distance[j] < min_weight:
                    min_weight = distance[j]
                    index_min_weight = j
            if min_weight == maxsize:
                break
            for z in range(n):
                if distance[index_min_weight] + matrix[index_min_weight][z] < distance[z]:
                    distance[z] = distance[index_min_weight] + matrix[index_min_weight][z]
            not_visited[index_min_weight] = False
        matrix[l] = distance

    for line in matrix:
        for elem in line:
            print(elem, end=' ', file=fout)
        print(file=fout)
    fout.close()


thread = threading.Thread(target=main)
thread.start()
