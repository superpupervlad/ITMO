from sys import setrecursionlimit, maxsize
import threading
from queue import Queue
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)


def main():
    fin = open("input.txt")
    fout = open("output.txt", "w")
    temp = []
    n, m = list(map(int, fin.readline().split())) #высота длина
    labyrinth = []
    for i in range(n):
        line = list(fin.readline())
        for j in range(m):
            if line[j] == '#':
                temp.append(None)
            elif line[j] == '.':
                temp.append([[], [], [], [], None, False, None, None]) #LRUD, dist, были?, prev, ссылка на prev
            elif line[j] == 'S':
                temp.append([[], [], [], [], None, False, None, None])
                start = [i, j]
            else:
                temp.append([[], [], [], [], None, False, None, None])
                end = [i, j]
        labyrinth.append(temp.copy())
        temp = []
    # print(labyrinth)
    for i in range(n):
        for j in range(m):
            if labyrinth[i][j] is not None:
                # Left
                if j == 0:
                    labyrinth[i][j][0] = None
                else:
                    labyrinth[i][j][0] = labyrinth[i][j - 1]
                # Right
                if j == m - 1:
                    labyrinth[i][j][1] = None
                else:
                    labyrinth[i][j][1] = labyrinth[i][j + 1]
                # Up
                if i == 0:
                    labyrinth[i][j][2] = None
                else:
                    labyrinth[i][j][2] = labyrinth[i - 1][j]
                # Down
                if i == n - 1:
                    labyrinth[i][j][3] = None
                else:
                    labyrinth[i][j][3] = labyrinth[i + 1][j]

    labyrinth[start[0]][start[1]][4] = 0
    #labyrinth = tuple(labyrinth)
    q = Queue()
    q.put(labyrinth[start[0]][start[1]])
    end_in_lab = labyrinth[end[0]][end[1]]
    while not q.empty():
        v = q.get()
        v[5] = True
        for i in range(4):
            if v[i] is not None:
                if v[i][5] is False:
                    v[i][4] = v[4] + 1
                    v[i][6] = i
                    v[i][7] = v
                    q.put(v[i])
                if id(v[i]) == id(end_in_lab):
                    break
    # print(start)
    # print(end)
    if end_in_lab[4] is None:
        print(-1, file = fout)
    else:
        path = []
        cur = end_in_lab
        for i in range(end_in_lab[4]):
            if cur[6] == 0:
                path.append('L')
            elif cur[6] == 1:
                path.append('R')
            elif cur[6] == 2:
                path.append('U')
            elif cur[6] == 3:
                path.append('D')
            cur = cur[7]
        print(end_in_lab[4], file = fout)
        for i in range(len(path)):
            print(path.pop(), end = '', file = fout)
    fout.close()

thread = threading.Thread(target=main)
thread.start()