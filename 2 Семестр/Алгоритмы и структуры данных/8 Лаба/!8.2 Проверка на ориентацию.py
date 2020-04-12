fin = open("input.txt")
fout = open("output.txt", "w")

n = int(fin.readline())
matrix = []
check = 0
for i in range(n):
    line = list(map(int, fin.readline().split()))
    matrix.append(line)
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            check = 1
            break
    if matrix[i][i] == 1 or check == 1:
        check = 1
        break
if check == 1:
    print('NO', file=fout)
else:
    print('YES', file=fout)
fout.close()
