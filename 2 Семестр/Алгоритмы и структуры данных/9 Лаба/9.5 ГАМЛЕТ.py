from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(134217728)

def main():
    def dfs(vertice, count):
        dfsed.add(vertice)
        graph[vertice][0] = True
        for i in range(1, len(graph[vertice])):
            next_vertice = graph[vertice][i]
            if graph[next_vertice][0] is None:
                if dfs(next_vertice, count + 1):
                    return True
        if count == n:
            print('YES', file = fout)
            return True
        graph[vertice][0] = None


    fin = open("hamiltonian.in")
    fout = open("hamiltonian.out", "w")
    n, m = list(map(int, fin.readline().split()))# Вершины Ребра
    graph = [[None] for _ in range(n)] # None не были
    for i in range(m):
        a, b = list(map(int, fin.readline().split()))
        graph[a - 1].append(b - 1)

    dfsed = set()
    for i in range(n):
        if i not in dfsed:
            if dfs(i, 1):
                break
    else:
        print('NO', file = fout)
    fout.close()

thread = threading.Thread(target=main)
thread.start()