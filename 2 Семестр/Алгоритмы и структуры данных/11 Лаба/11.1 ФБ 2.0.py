from sys import setrecursionlimit, maxsize
import threading

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
    edges = []

    for i in range(n):
        temp = list(map(int, fin.readline().split()))
        for j in range(len(temp)):
            if temp[j] != -1 or j == i:
                edges.append([i, j, temp[j]])

    for i in range(n):
        check = False
        for j in range(len(edges)):
            if distance[edges[j][1]] > distance[edges[j][0]] + edges[j][2]:
                distance[edges[j][1]] = distance[edges[j][0]] + edges[j][2]
                check = True
        if not check:
            break
        if distance[f] == inf:
            print(-1, file=fout)
        else:
            print(distance[f], file=fout)
    fout.close()


thread = threading.Thread(target=main)
thread.start()
