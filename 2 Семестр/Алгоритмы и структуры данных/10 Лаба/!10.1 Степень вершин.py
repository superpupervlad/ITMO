from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(134217728)

def main():
    fin = open("input.txt")
    fout = open("output.txt", "w")
    n, m = list(map(int, fin.readline().split()))# Вершины Ребра
    graph = [0 for _ in range(n)]

    for i in range(m):
        a, b = list(map(int, fin.readline().split()))
        graph[a - 1] += 1
        graph[b - 1] += 1
    for v in graph:
        print(v, end = ' ', file = fout)
    fout.close()

thread = threading.Thread(target=main)
thread.start()