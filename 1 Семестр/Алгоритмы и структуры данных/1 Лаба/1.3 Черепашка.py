fin = open("turtle.in")
fout = open("turtle.out","w")
h, w = list(map(int,fin.readline().split()))
b = []
for i in range(h):
    b.append(list(map(int,fin.readline().split())))
for i in range(h - 2, -1, -1):
    b[i][0] += b[i+1][0]
for i in range(1, w):
    b[-1][i] += b[-1][i - 1]
for i in range(1, w):
    for j in range(h - 2, -1, -1):
        if b[j][i-1] > b[j+1][i]:
            b[j][i] += b[j][i-1]
        else:
            b[j][i] += b[j+1][i]
print(b[0][-1],file = fout)
fout.close()