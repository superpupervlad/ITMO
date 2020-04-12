fin = open("input.txt")
fout = open("output.txt", "w")

n, m = list(map(int, fin.readline().split()))
matrix = [[0] * n for _ in range(n)]
check = 0

for i in range(m):
    t = list(map(int, fin.readline().split()))
    matrix[t[0] - 1][t[1] - 1] += 1
    matrix[t[1] - 1][t[0] - 1] += 1
for i in range(n):
    for j in range(n):
        if matrix[i][j] > 1:
            check = 1
            break
if check == 1:
    print('YES', file=fout)
else:
    print('NO', file=fout)
fout.close()
