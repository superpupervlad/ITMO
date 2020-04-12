#  1. Используй Дейкстру, можно даже без кучи
from sys import setrecursionlimit, maxsize
import threading
import array
setrecursionlimit(10 ** 9)
threading.stack_size(260000000)


def main():
    fin = open("pathmgep.in")
    fout = open("pathmgep.out", "w")
    inf = maxsize
    n, s, f = list(map(int, fin.readline().split()))
    distance = [inf] * n
    s, f = s - 1, f - 1
    distance[s] = 0
    matrix = []

    for i in range(n):
        matrix.append(list(map(int, fin.readline().replace('-1', str(maxsize)).split())))

    not_visited = array.array('b', [1] * n)
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

    if distance[f] == inf:
        print(-1, file = fout)
    else:
        print(distance[f], file = fout)
    fout.close()


thread = threading.Thread(target=main)
thread.start()
