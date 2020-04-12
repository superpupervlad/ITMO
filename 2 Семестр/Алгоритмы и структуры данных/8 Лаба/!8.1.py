fin = open("input.txt")
fout = open("output.txt", "w")

n, m = list(map(int, fin.readline().split()))
matrix = [[0] * n for _ in range(n)]
for i in range(m):
    t = list(map(int, fin.readline().split()))
    matrix[t[0] - 1][t[1] - 1] = 1
for elem in matrix:
    for i in range(n):
        print(elem[i], end = ' ', file = fout)
    print(file = fout)
fout.close()
