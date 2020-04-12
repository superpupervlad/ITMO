from sys import setrecursionlimit, maxsize
import threading
import array
setrecursionlimit(10 ** 9)
threading.stack_size(260000000)


def main():
    fin = open("pathbgep.in")
    fout = open("pathbgep.out", "w")
    inf = 1000000
    n, m = list(map(int, fin.readline().split()))
    distance = array.array('L', [inf] * n)
    distance[0] = 0
    matrix = [array.array('l', [inf for _ in range(n)]) for _ in range(n)]

    for i in range(m):
        a, b, cost = list(map(int, fin.readline().split()))
        a, b = a - 1, b - 1
        matrix[a][b], matrix[b][a] = cost, cost

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
        not_visited[index_min_weight] = 0

    fout.write(' '.join(str(a) for a in distance))
    fout.close()


thread = threading.Thread(target=main)
thread.start()
