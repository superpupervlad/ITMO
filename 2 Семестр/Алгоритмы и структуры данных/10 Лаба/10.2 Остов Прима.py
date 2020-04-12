from sys import setrecursionlimit, maxsize
from math import sqrt
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(134217728)

def main():
    fin = open("spantree.in")
    fout = open("spantree.out", "w")
    n = int(fin.readline())
    graph = [[None for i in range(n)] for _ in range(n)]
    coordinates = [None for _ in range(n)]
    print(graph)
    for i in range(n):
        x, y = list(map(int, fin.readline().split()))
        x -= 1
        y -= 1
        coordinates[i] = [x, y]
    for i in range(n):
        for j in range(n):
            l = sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
            graph[i][j] = l
            graph[j][i] = l
    print(graph)
    #visited = [False for _ in range(n)]
    visited = []
    path_lenght = 0
    visited.append(0)
    for i in range(n):
        next_v = min(min(graph[g]) for j in range(len(visited)))
        min = maxsize



        path_lenght += next_v

    fout.close()

thread = threading.Thread(target=main)
thread.start()