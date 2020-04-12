"""ЗАПУСКАЕМ
░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░
▄███▀░◐░░░▌░░░░░░░
░░░░▌░░░░░▐░░░░░░░
░░░░▐░░░░░▐░░░░░░░
░░░░▌░░░░░▐▄▄░░░░░
░░░░▌░░░░▄▀▒▒▀▀▀▀▄
░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄
░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░▄▄▌▌▄▌▌░░░░░
1. Есть параллельные ребра"""
from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(260000000)

def main():
    def find(ver):
        nonlocal parent
        if parent[ver] == ver:
            return ver
        return find(parent[ver])

    def union():
        nonlocal parent, rank, edges_in_mst, a, b, cost, s
        a_ = find(a)
        b_ = find(b)
        if a_ != b_:
            if rank[a_] < rank[b_]:
                parent[a_] = b_
            elif rank[a_] > rank[b_]:
                parent[b_] = a_
            else:
                parent[b_] = a_
                rank[a_] += 1
            edges_in_mst += 1
            s += cost

    fin = open("spantree3.in")
    fout = open("spantree3.out", "w")
    edges_in_mst = 0
    n, m = list(map(int, fin.readline().split()))
    edges, s = [], 0
    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]

    for i in range(m):
        a, b, cost = list(map(int, fin.readline().split()))
        edges.append([cost, a - 1, b - 1])
    edges.sort()

    i = 0
    while edges_in_mst < (n - 1):
        cost, a, b = edges[i]
        union()
        i += 1

    print(s, file = fout)
    fout.close()

thread = threading.Thread(target=main)
thread.start()