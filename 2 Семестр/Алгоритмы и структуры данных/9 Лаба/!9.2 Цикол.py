from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(134217728)

def main():
    def dfs(vertice):
        nonlocal cycle_start
        graph[vertice][0] = 1
        path.append(vertice + 1)
        for i in range(1, len(graph[vertice])):
            next_ver = graph[vertice][i]
            if graph[next_ver][0] == 0:
                if dfs(graph[vertice][i]):
                    stack.append(vertice + 1)
                    return True
            elif graph[next_ver][0] == 1:
                stack.append(vertice + 1)
                cycle_start = next_ver + 1
                return True
        graph[vertice][0] = 2
        path.pop()

    fin = open("cycle.in")
    fout = open("cycle.out", "w")
    n, m = list(map(int, fin.readline().split()))# Вершины Ребра
    graph = [[0] for _ in range(n)]
    cycle_start = None

    for i in range(m):
        a, b = list(map(int, fin.readline().split()))
        graph[a - 1].append(b - 1)
    path = []
    stack = []
    final = []
    for i in range(len(graph)):
        if graph[i][0] == 0:
            if dfs(i):
                print('YES', file=fout)
                for elem in stack:
                    if elem != cycle_start:
                        final.append(elem)
                    else:
                        final.append(elem)
                        break
                for i in range(path.index(cycle_start), len(path)):
                    print(path[i], end=' ', file=fout)
                break
    else:
        print('NO', file=fout)

    #print(path)
    fout.close()

thread = threading.Thread(target=main)
thread.start()