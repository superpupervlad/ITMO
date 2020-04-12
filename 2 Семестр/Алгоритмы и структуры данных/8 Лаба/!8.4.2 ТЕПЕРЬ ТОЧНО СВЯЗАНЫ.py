from sys import setrecursionlimit, maxsize
import threading

setrecursionlimit(10 ** 9)
threading.stack_size(67108864)


def main():
    def dfs(dot, n_component):
        info[dot][0] = 1
        info[dot][1] = n_component
        for i in range(len(matrix[dot])):
            new_dot = matrix[dot][i]
            if info[new_dot][0] == 0:
                dfs(new_dot, n_component)

    fin = open("components.in")
    fout = open("components.out", "w")

    # n - Количетсво вершин  m - Количество ребер
    n, m = list(map(int, fin.readline().split()))
    matrix = [[] for _ in range(n)]
    info = [[0, -1] for _ in range(n)]
    count = 1
    for i in range(m):
        temp = list(map(int, fin.readline().split()))
        if temp[1] - 1 not in matrix[temp[0] - 1]:
            matrix[temp[0] - 1].append(temp[1] - 1)
        if temp[0] - 1 not in matrix[temp[1] - 1]:
            matrix[temp[1] - 1].append(temp[0] - 1)

    for i in range(n):
        if info[i][0] == 0:
            dfs(i, count)
            count += 1
    print(count - 1, file=fout)
    for i in range(n):
        print(info[i][1], end=' ', file=fout)
    # print(matrix)
    # print(info)
    fout.close()


thread = threading.Thread(target=main)
thread.start()
