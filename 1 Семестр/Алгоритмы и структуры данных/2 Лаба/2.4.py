fin = open("antiqs.in")
fout = open("antiqs.out", "w")
n = list(map(int, fin.readline().split()))
n = n[0]
for i in range(1, n//2 + 1):
    print(i, file = fout, end = ' ')
print(n, file = fout, end = ' ')
for i in range(n//2 + 1, n - 1):
    print(i, file = fout, end = ' ')
fout.close()
#2.4 Анти QS