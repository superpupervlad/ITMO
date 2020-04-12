def dfs(dot, lenght):
    info[dot][0] = 1  # Помечаем были ли мы здесь
    check = 0
    if info[dot][1] > lenght or info[dot][1] is None:  # Делаем расстояние минимальным
        info[dot][1] = lenght
        check = 1
    for i in range(len(matrix[dot])):
        new_dot = matrix[dot][i]
        if info[new_dot][0] == 0 and new_dot != 0:
            dfs(new_dot, lenght + 1)


fin = open("pathbge1.in")
fout = open("pathbge1.out", "w")

# n - Количетсво вершин  m - Количество ребер
n, m = list(map(int, fin.readline().split()))
matrix = [[] for _ in range(n)]
info = [[0, None] for _ in range(n)]  # 0-Были ли 1-расстояние 2?
count = 1

for i in range(m):
    temp = list(map(int, fin.readline().split()))
    if temp[1] - 1 not in matrix[temp[0] - 1]:
        matrix[temp[0] - 1].append(temp[1] - 1)
    if temp[0] - 1 not in matrix[temp[1] - 1]:
        matrix[temp[1] - 1].append(temp[0] - 1)


dfs(0, 0)
count += 1

for i in range(n):
    print(info[i][1], end=' ', file=fout)
# print(matrix)
# print(info)
fout.close()
