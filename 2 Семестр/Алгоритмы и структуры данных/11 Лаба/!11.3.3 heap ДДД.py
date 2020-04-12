# 1. Юзай кучу
from sys import setrecursionlimit, maxsize
import threading
import array
from heapq import heappush, heappop
setrecursionlimit(10 ** 9)
threading.stack_size(260000000)


def main():
    fin = open("pathbgep.in")
    fout = open("pathbgep.out", "w")
    inf = 1000000
    n, m = list(map(int, fin.readline().split()))
    distance = array.array('L', [inf] * n)
    distance[0] = 0
    matrix = [{} for _ in range(n)]

    for i in range(m):
        a, b, cost = list(map(int, fin.readline().split()))
        a, b = a - 1, b - 1
        matrix[a][b], matrix[b][a] = cost, cost

    distance = [None] * n
    q = [(0, 0)]
    while q:
        path_len, v = heappop(q)
        if distance[v] is None:
            distance[v] = path_len
            for another_v, edge_len in matrix[v].items():
                if distance[another_v] is None:
                    heappush(q, (path_len + edge_len, another_v))

    fout.write(' '.join(str(a) for a in distance))
    fout.close()


thread = threading.Thread(target=main)
thread.start()
