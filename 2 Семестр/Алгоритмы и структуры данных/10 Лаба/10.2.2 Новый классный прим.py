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
from sys import setrecursionlimit
import heapq
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(134217728)

def main():
    def dist(x1, x2, y1, y2):
        return (x2 - x1)**2 + (y2 - y1)**2


    def add_few_elements_in_heap(index):
        nonlocal edges_from_tree
        nonlocal vertices_in_tree
        nonlocal graph
        for elem in graph[index]:
            heapq.heappush(edges_from_tree, elem)
        vertices_in_tree.add(index)
        graph[index] = None


    fin = open("spantree.in")
    fout = open("spantree.out", "w")
    n = int(fin.readline())
    graph = [[] for _ in range(n)]
    coordinates = [[0, 0] for _ in range(n)]
    sum = 0

    for i in range(n):
        x, y = list(map(int, fin.readline().split()))
        coordinates[i][0] = x
        coordinates[i][1] = y
    coordinates = tuple(coordinates)

    for i in range(n):
        x1 = coordinates[i][0]
        y1 = coordinates[i][1]
        for j in range(n):
            x2 = coordinates[j][0]
            y2 = coordinates[j][1]
            if x1 == x2 and y1 == y2:
                continue
            graph[i].append([dist(x1,x2,y1,y2), j])

    del coordinates
    vertices_in_tree = {0}
    edges_from_tree = []
    add_few_elements_in_heap(0)

    for i in range(n - 1):
        nearest = heapq.heappop(edges_from_tree)
        while nearest[1] in vertices_in_tree:
            nearest = heapq.heappop(edges_from_tree)
        add_few_elements_in_heap(nearest[1])
        sum += nearest[0]**0.5

    print(sum, file = fout)
    fout.close()

thread = threading.Thread(target=main)
thread.start()