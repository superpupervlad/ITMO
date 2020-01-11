fin = open("isheap.in")
fout = open("isheap.out", "w")
n = int(fin.readline())
a = list(map(int, fin.readline().split()))
check = 0
for i in range(1, n//2):
    if a[i - 1] > a[2*i - 1] or a[i - 1] > a[2*i]:
        check = 1
        break
if check == 0:
    print("YES", file=fout)
else:
    print("NO", file=fout)
fout.close()