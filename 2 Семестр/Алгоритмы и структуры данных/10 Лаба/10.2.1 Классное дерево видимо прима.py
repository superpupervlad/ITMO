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
░░░░░░░░░▄▄▌▌▄▌▌░░░░░"""
from sys import setrecursionlimit, maxsize
import heapq
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(134217728)

def main():
    def dist(x1, x2, y1, y2):
        return (x2 - x1)**2 + (y2 - y1)**2

    inf = maxsize
    fin = open("spantree.in")
    fout = open("spantree.out", "w")
    n = int(fin.readline())
    not_in_tree = [[[], _, False] for _ in range(n)]
    coordinates = [[0, 0] for _ in range(n)]
    sum = 0

    for i in range(n):
        x, y = list(map(int, fin.readline().split()))
        coordinates[i][0] = x
        coordinates[i][1] = y

    for i in range(n):
        x1 = coordinates[i][0]
        y1 = coordinates[i][1]
        for j in range(n):
            x2 = coordinates[j][0]
            y2 = coordinates[j][1]
            if x1 == x2 and y1 == y2:
                continue
            heapq.heappush(not_in_tree[i][0], [dist(x1, x2, y1, y2), j])
    tree = [not_in_tree[0]]
    not_in_tree[0][2] = True
    for i in range(n - 1):
        while True: # Чекаем нет ли уже вершины в дереве
            nearest_index = tree.index(min(tree))
            nearest = heapq.heappop(tree[nearest_index][0])
            if len(not_in_tree[nearest_index][0]) == 0:
                not_in_tree[nearest_index][0].append(inf)
            if not not_in_tree[nearest[1]][2]:
                break
        not_in_tree[nearest[1]][2] = True
        tree.append(not_in_tree[nearest[1]])
        sum += nearest[0]**0.5
    print(sum, file = fout)
    fout.close()

thread = threading.Thread(target=main)
thread.start()