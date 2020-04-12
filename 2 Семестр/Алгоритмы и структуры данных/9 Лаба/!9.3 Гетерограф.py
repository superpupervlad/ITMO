from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(134217728)

def main():
    def dfs(vertice, set):
        graph[vertice][0] = set
        for i in range(1, len(graph[vertice])):
            next_vertice = graph[vertice][i]
            if graph[next_vertice][0] is None:
                if dfs(next_vertice, not set):
                    return True
            elif graph[next_vertice][0] == set:
                print('NO', file=fout)
                return True


    fin = open("bipartite.in")
    fout = open("bipartite.out", "w")
    n, m = list(map(int, fin.readline().split()))# Вершины Ребра
    graph = [[None] for _ in range(n)] # None не были

    for i in range(m):
        a, b = list(map(int, fin.readline().split()))
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    for i in range(len(graph)):
        if graph[i][0] is None:
            if dfs(i, True):
                break
    else:
        print('YES', file=fout)
    fout.close()

thread = threading.Thread(target=main)
thread.start()