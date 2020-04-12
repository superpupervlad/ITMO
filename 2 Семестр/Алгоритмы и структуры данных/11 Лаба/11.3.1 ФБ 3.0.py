from sys import setrecursionlimit, maxsize
import threading

setrecursionlimit(10 ** 9)
threading.stack_size(260000000)


def main():
    fin = open("pathbgep.in")
    fout = open("pathbgep.out", "w")

    inf = maxsize
    n, m = list(map(int, fin.readline().split()))
    distance = [inf] * n
    distance[0] = 0
    edges = []

    for i in range(m):
        t = list(map(int, fin.readline().split()))
        t[0] -= 1
        t[1] -= 1
        edges.append(t.copy())
        edges.append([t[1], t[0], t[2]].copy())

    for i in range(n):
        check = False
        for j in range(2 * m):
            if distance[edges[j][1]] > distance[edges[j][0]] + edges[j][2]:
                distance[edges[j][1]] = distance[edges[j][0]] + edges[j][2]
                check = True
        if not check:
            break

    fout.write(' '.join(str(a) for a in distance))
    fout.close()


thread = threading.Thread(target=main)
thread.start()
