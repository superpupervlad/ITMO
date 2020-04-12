from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(134217728)

def main():
    def dfs(vertice):
        graph[vertice][0] = 1
        for i in range(1, len(graph[vertice])):
            next_ver = graph[vertice][i]
            if graph[next_ver][0] == 0:
                if dfs(graph[vertice][i]):
                    return True
            elif graph[next_ver][0] == 1:
                return True
        graph[vertice][0] = 2
        answer.append(vertice + 1)

    fin = open("topsort.in")
    fout = open("topsort.out", "w")
    n, m = list(map(int, fin.readline().split()))# Вершины Ребра
    graph = [[0] for _ in range(n)]

    for i in range(m):
        a, b = list(map(int, fin.readline().split()))
        graph[a - 1].append(b - 1)
    answer = []
    for i in range(len(graph)):
        if graph[i][0] == 0:
            if dfs(i):
                print(-1, file = fout)
                break
    else:
        for i in range(len(answer)):
            print(answer.pop(), end = ' ', file = fout)
    fout.close()

thread = threading.Thread(target=main)
thread.start()