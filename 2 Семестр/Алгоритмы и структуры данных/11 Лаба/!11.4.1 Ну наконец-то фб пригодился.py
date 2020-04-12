from sys import setrecursionlimit
import threading

setrecursionlimit(10 ** 9)
threading.stack_size(260000000)


def main():
    def dfs(v):
        visited.add(v)
        for vertice in graph[v]:
            if vertice not in visited:
                dfs(vertice)

    fin = open("path.in")
    fout = open("path.out", "w")

    inf = 10 ** 20
    n, m, s = list(map(int, fin.readline().split()))
    distance = [inf] * n
    distance[s - 1] = 0
    edges = []
    path = [None] * n
    graph = [[] for _ in range(n)]

    for i in range(m):
        a, b, cost = list(map(int, fin.readline().split()))
        a -= 1
        b -= 1
        edges.append([a, b, cost])
        graph[a].append(b)

    for i in range(n):
        c = 'a'
        for j in range(m):
            if distance[edges[j][0]] != inf:
                if distance[edges[j][1]] > distance[edges[j][0]] + edges[j][2]:
                    distance[edges[j][1]] = distance[edges[j][0]] + edges[j][2]
                    path[edges[j][1]] = edges[j][0]
                    c = edges[j][1]
        if c == 'a':
            break

    if c != 'a':
        for i in range(n):
            c = path[c]
        final_path = []
        cur = c
        visited = set()
        dfs(c)
        while True:
            cur = path[cur]
            final_path.append(cur)
            if cur == c and len(final_path) > 1:
                break

        while visited:
            distance[visited.pop()] = '-'

    for elem in distance:
        if elem == inf:
            print('*', file=fout)
        else:
            print(elem, file=fout)
    fout.close()


thread = threading.Thread(target=main)
thread.start()