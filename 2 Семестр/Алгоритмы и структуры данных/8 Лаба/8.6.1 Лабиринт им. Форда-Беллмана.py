def check_left_right(id, line): # это очень плохо но мне лень переписывать
    global edges
    global m
    global cells
    global start
    global end
    if line[0] == 'S':
        start = id
    if line[0] == 'T':
        end = id
    if line[-1] == 'S':
        start = id + m - 1
    if line[-1] == 'T':
        end = id + m - 1
    if line[0] != '#' and line[1] != '#':
        edges[1].append([id, id + 1])
    if line[-1] != '#' and line[-2] != '#':
        edges[0].append([id + m - 1, id + m - 2])
    for i in range(1, m - 1):
        if line[i] == '.':
            cells.append(id + i)
            if line[i - 1] != '#':
                edges[0].append([id + i, id + i - 1])
            if line[i + 1] != '#':
                edges[1].append([id + i, id + i + 1])
        elif line[i] == 'S':
            cells.append(id + i)
            if line[i - 1] != '#':
                edges[0].append([id + i, id + i - 1])
            if line[i + 1] != '#':
                edges[1].append([id + i, id + i + 1])
            start = id + i
        elif line[i] == 'T':
            cells.append(id + i)
            if line[i - 1] != '#':
                edges[0].append([id + i, id + i - 1])
            if line[i + 1] != '#':
                edges[1].append([id + i, id + i + 1])
            end = id + i

def check_up_down(id, line1, line2):
    global edges
    global m
    for i in range(m):
        if line1[i] != '#' != line2[i]:
            edges[3].append([id + i, id + i + m])
            edges[2].append([id + i, id + i + m])

import sys
fin = open("input.txt")
fout = open("output.txt", "w")
inf = sys.maxsize
cells = []
temp = []
n, m = list(map(int, fin.readline().split())) #высота длина
labyrinth = []

distance = [inf for _ in range(n*m)]
edges = [[], [], [], []]
cur = list(fin.readline()[:-1])

for i in range(n - 1):
    next = list(fin.readline()[:-1])
    check_left_right(i * m, cur)
    check_up_down(i * m, cur, next)
    cur = next.copy()
check_left_right((n - 1) * m, cur)
distance[start] = 0
edges = tuple(edges)
lr = len(edges[0])
ud = len(edges[2])
path = [None for _ in range(n*m)]
while True:
    check = False
    for i in 0,1:
        for j in range(lr):
            if distance[edges[i][j][1]] > distance[edges[i][j][0]] + 1:
                distance[edges[i][j][1]] = distance[edges[i][j][0]] + 1
                if i == 0:
                    path[edges[i][j][1]] = 'L'
                if i == 1:
                    path[edges[i][j][1]] = 'R'
                check = True
    for i in 2,3:
        for j in range(ud):
            if distance[edges[i][j][1]] > distance[edges[i][j][0]] + 1:
                distance[edges[i][j][1]] = distance[edges[i][j][0]] + 1
                if i == 2:
                    path[edges[i][j][1]] = 'D'
                if i == 3:
                    path[edges[i][j][1]] = 'U'
                check = True
    if not check:
        break
# print(distance)
# print(edges)
# print(path)
final_path = []
cur = end
edges = None
print(distance[end], file = fout)
for i in range(distance[end]):
    final_path.append(path[cur])
    if path[cur] == 'L':
        cur += 1
    elif path[cur] == 'R':
        cur -= 1
    elif path[cur] == 'U':
        cur += m
    elif path[cur] == 'D':
        cur -= m
for i in range(len(final_path)):
    print(final_path.pop(), end = '', file = fout)
fout.close()
