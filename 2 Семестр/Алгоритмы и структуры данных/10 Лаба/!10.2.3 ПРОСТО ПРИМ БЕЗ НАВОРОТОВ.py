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
1.  Нужно оптимально написать Прима
2.  List - плохо по памяти, хорошо по скорости
    Array - хорошо по памяти, плохо по скорости (пушто там хранятся необработанные байты и  когда
    мы обращаемся к элементу массива, создается элемент класса)
    Нужно правильно подобрать соотношение скорости/памяти"""
from sys import setrecursionlimit, maxsize
import threading
import array
setrecursionlimit(10 ** 9)
threading.stack_size(260000000)

def main():
    def dist(x1, x2, y1, y2):
        return (x2 - x1)**2 + (y2 - y1)**2


    fin = open("spantree.in")
    fout = open("spantree.out", "w")
    inf = maxsize
    n = int(fin.readline())
    graph = [array.array('l') for _ in range(n)]
    coordinates = [[0, 0] for _ in range(n)]

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
            graph[i].append(dist(x1,x2,y1,y2))
    del coordinates

    distances = [inf for _ in range(n)]
    visited = array.array('b', [0 for _ in range(n)])
    distances[0] = 0
    for i in range(n):
        cur = None
        for j in range(n):
            if not visited[j] and (cur is None or distances[j] < distances[cur]):
                cur = j
        visited[cur] = 1
        for ver in range(n):
            if not visited[ver] and graph[cur][ver] < distances[ver] and ver is not cur:
                distances[ver] = graph[cur][ver]

    print(sum(elem**0.5 for elem in distances), file = fout)
    fout.close()

thread = threading.Thread(target=main)
thread.start()