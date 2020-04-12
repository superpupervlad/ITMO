from sys import setrecursionlimit
import threading

setrecursionlimit(10 ** 9)
threading.stack_size(134217728)


def main():
    def dfs(vertice):
        not_oriented_graph[vertice][0] = True
        nonlocal count
        count += 1
        for i in range(1, len(not_oriented_graph[vertice])):
            next_vertice = not_oriented_graph[vertice][i]
            if not_oriented_graph[next_vertice][0] is None:
                dfs(next_vertice)

    fin = open("hamiltonian.in")
    fout = open("hamiltonian.out", "w")
    n, m = list(map(int, fin.readline().split()))  # Вершины Ребра
    not_oriented_graph = [[None] for _ in range(n)]
    got_in = {i for i in range(1, n + 1)}
    got_out = {i for i in range(1, n + 1)}

    for i in range(m):
        a, b = list(map(int, fin.readline().split()))
        not_oriented_graph[a - 1].append(b - 1)
        not_oriented_graph[b - 1].append(a - 1)
        got_in.discard(b)
        got_out.discard(a)


    count = 0
    dfs(0)
    if count != n or len(got_in) > 1 or len(got_out) > 1:
        print('NO', file=fout)
    elif len(got_out) == 1:
        if len(not_oriented_graph[got_out.pop() - 1]) > 3:
            print('NO', file=fout)
    else:
        print('YES', file=fout)

    fout.close()


thread = threading.Thread(target=main)
thread.start()