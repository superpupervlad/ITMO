from math import inf
from sys import setrecursionlimit
from _collections import deque
import threading

setrecursionlimit(10 ** 9)
threading.stack_size(260000000)


def main():
    def bfs():
        arr[0] = 1
        q = deque()
        q.append(0)
        while q and not arr[sink]:
            cur = q.popleft()
            for edge in graph[cur]:
                if not arr[edges[edge][1]] and edges[edge][2] > edges[edge][3]: #cost > flow
                    q.append(edges[edge][1])
                    arr[edges[edge][1]] = arr[cur] + 1
        return arr[sink]

    def dfs(ver, flow):
        if flow == 0 or ver == sink:
            return flow
        while cur[ver] < len(graph[ver]):
            edge = graph[ver][cur[ver]]
            if arr[ver] + 1 == arr[edges[edge][1]]:
                r = dfs(edges[edge][1], min(flow, edges[edge][2] - edges[edge][3]))
                if r != 0:
                    edges[edge][3] += r
                    edges[edge ^ 1][3] -= r
                    return r
            cur[ver] += 1
        return 0

    def read(a, b, cost):
        graph[a].append(len(edges))
        edges.append([a, b, cost, 0])
        graph[b].append(len(edges))
        edges.append([b, a, 0, 0])

    fin = open("circulation.in")
    fout = open("circulation.out", "w")

    n, m = list(map(int, fin.readline().split()))
    n += 2
    sink = n - 1
    edges = []
    graph = [[] for _ in range(n)]
    cur = [0] * n

    for i in range(m):
        a, b, lcost, hcost = list(map(int, fin.readline().split()))
        read(0, b, lcost)
        read(a, b, hcost - lcost)
        read(a, sink, lcost)

    graph = tuple(graph)
    arr = [0] * n
    while bfs():
        while dfs(0, inf):
            continue
        cur = [0] * n
        arr = [0] * n

    for edge in graph[0]:
        if edges[edge][3] < edges[edge][2]:
            print('NO', file = fout)
            break
    else:
        print('YES', file = fout)
        for i in range(0, len(edges), 6):
            print(edges[i + 2][3] + edges[i + 4][3], file = fout)


thread = threading.Thread(target=main)
thread.start()
