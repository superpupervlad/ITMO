from sys import setrecursionlimit, maxsize
import threading

setrecursionlimit(10 ** 9)
threading.stack_size(260000000)


def main():
    fin = open("negcycle.in")
    fout = open("negcycle.out", "w")
    inf = 10 ** 9
    n = int(fin.readline())
    distance = [0] * n
    edges = []
    path = [None] * n

    for i in range(n):
        x = list(map(int, fin.readline().split()))
        for j in range(n):
            if x[j] != inf:
                edges.append([i, j, x[j]])

    for i in range(n):
        c = 'a'
        for j in range(len(edges)):
            if distance[edges[j][1]] > distance[edges[j][0]] + edges[j][2]:
                distance[edges[j][1]] = max(-inf, distance[edges[j][0]] + edges[j][2])
                path[edges[j][1]] = edges[j][0]
                c = edges[j][1]
        if c == 'a':
            break

    if c != 'a':
        for i in range(n):
            c = path[c]
        final_path = []
        cur = c
        while True:
            final_path.append(cur)
            cur = path[cur]
            if cur == c:
                break
        final_path.append(cur)
        final_path.reverse()

        fout.write('YES\n')
        fout.write(str(len(final_path)) + '\n')
        fout.write(' '.join(str(a + 1) for a in final_path))
    else:
        fout.write('NO')
    fout.close()


thread = threading.Thread(target=main)
thread.start()