from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(134217728)

def main():
    def inv_dfs(vertice):
        inverted_graph[vertice][0] = True
        for i in range(1, len(inverted_graph[vertice])):
            next_vertice = inverted_graph[vertice][i]
            if inverted_graph[next_vertice][0] is None:
                inv_dfs(next_vertice)
        exit_time.append(vertice)


    def dfs(vertice, count):
        graph[vertice][0] = True
        con_id[vertice] = count
        for i in range(1, len(graph[vertice])):
            next_vertice = graph[vertice][i]
            if graph[next_vertice][0] is None:
                dfs(next_vertice, count)


    fin = open("cond.in")
    fout = open("cond.out", "w")
    n, m = list(map(int, fin.readline().split()))# Вершины Ребра
    graph = [[None] for _ in range(n)] # None не были
    inverted_graph = [[None] for _ in range(n)]
    exit_time = []
    for i in range(m):
        a, b = list(map(int, fin.readline().split()))
        graph[a - 1].append(b - 1)
        inverted_graph[b - 1].append(a - 1)

    for i in range(n):
        if inverted_graph[i][0] is None:
            inv_dfs(i)

    count = 1
    con_id = [[None] for _ in range(n)]
    while exit_time:
        v = exit_time.pop()
        if graph[v][0] is None:
            dfs(v, count)
            count += 1
    print(count - 1, file = fout)
    for i in range(n):
        #con_id[i] = count - con_id[i]
        print(count - con_id[i], end = ' ', file = fout)
    fout.close()

thread = threading.Thread(target=main)
thread.start()