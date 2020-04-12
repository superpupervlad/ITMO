from sys import setrecursionlimit
import threading

setrecursionlimit(10 ** 9)
threading.stack_size(134217728)


def main():
    def dfs(vertice, count):
        inv_graph[vertice][0] = True
        if count == n:
            print('YES', file=fout)
            return True
        for i in range(1, len(inv_graph[vertice])):
            next_vertice = inv_graph[vertice][i]
            if inv_graph[next_vertice][0] is None:
                if dfs(next_vertice, count + 1):
                    return True
        inv_graph[vertice][0] = None

    fin = open("hamiltonian.in")
    fout = open("hamiltonian.out", "w")
    n, m = list(map(int, fin.readline().split()))  # Вершины Ребра
    inv_graph = [[None] for _ in range(n)]
    not_got_out = {i for i in range(1, n + 1)}

    for i in range(m):
        a, b = list(map(int, fin.readline().split()))
        inv_graph[b - 1].append(a - 1)
        not_got_out.discard(a)

    if not dfs(not_got_out.pop() - 1, 1):
        print('NO', file=fout)

    fout.close()


thread = threading.Thread(target=main)
thread.start()