from sys import setrecursionlimit, maxsize
import threading
from queue import Queue
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)


def main():
    fin = open("input.txt")
    fout = open("output.txt", "w")
    n, m = list(map(int, fin.readline().split())) #высота длина
    labyrinth = [] #[[None for i in range(m)] for _ in range(n)]
    prev = [[False for i in range(m)] for _ in range(n)]
    distance = [[None for i in range(m)] for _ in range(n)]
    for i in range(n):
        temp = list(fin.readline()[:-1])
        for j in range(m):
            if temp[j] == '.':
                temp[j] = True
            elif temp[j] == '#':
                temp[j] = False
            elif temp[j] == 'T':
                temp[j] = True
                end = [i, j]
            elif temp[j] == 'S':
                temp[j] = True
                start = [i, j]
        labyrinth.append(temp)
    q = Queue()
    q.put(start)
    distance[start[0]][start[1]] = 0
    while not q.empty():
        cur_i, cur_j = q.get()

        if cur_j - 1 > -1:
            if labyrinth[cur_i][cur_j - 1] and distance[cur_i][cur_j - 1] is None: # Left
                distance[cur_i][cur_j - 1] = distance[cur_i][cur_j] + 1
                prev[cur_i][cur_j - 1] = 'L'
                q.put([cur_i, cur_j - 1])
        if cur_j + 1 < m:
            if labyrinth[cur_i][cur_j + 1] and distance[cur_i][cur_j + 1] is None: # Right
                distance[cur_i][cur_j + 1] = distance[cur_i][cur_j] + 1
                prev[cur_i][cur_j + 1] = 'R'
                q.put([cur_i, cur_j + 1])
        if cur_i - 1 > -1:
            if labyrinth[cur_i - 1][cur_j] and distance[cur_i - 1][cur_j] is None: # Up
                distance[cur_i - 1][cur_j] = distance[cur_i][cur_j] + 1
                prev[cur_i - 1][cur_j] = 'U'
                q.put([cur_i - 1, cur_j])
        if cur_i + 1 < n:
            if labyrinth[cur_i + 1][cur_j] and distance[cur_i + 1][cur_j] is None: # Up
                distance[cur_i + 1][cur_j] = distance[cur_i][cur_j] + 1
                prev[cur_i + 1][cur_j] = 'D'
                q.put([cur_i + 1, cur_j])
        if distance[end[0]][end[1]] is not None:
            break
    cur_i, cur_j = end
    path = []

    if distance[cur_i][cur_j] is None:
        print(-1, file = fout)
    else:
        print(distance[cur_i][cur_j], file = fout)
        for i in range(distance[cur_i][cur_j]):
            if prev[cur_i][cur_j] == 'L':
                path.append('L')
                cur_j += 1
            elif prev[cur_i][cur_j] == 'R':
                path.append('R')
                cur_j -= 1
            elif prev[cur_i][cur_j] == 'U':
                path.append('U')
                cur_i += 1
            elif prev[cur_i][cur_j] == 'D':
                path.append('D')
                cur_i -= 1
    # for elem in distance:
    #     print('d' + str(elem))
    # for elem in prev:
    #     print('p' + str(elem))
    # for elem in labyrinth:
    #     print('l' + str(elem))
    # print(path)
        for i in range(len(path)):
            print(path.pop(), end='', file=fout)

    fout.close()

thread = threading.Thread(target=main)
thread.start()