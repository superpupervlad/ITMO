fin = open("garland.in")
fout = open("garland.out", "w")
n, a = list(map(float, fin.readline().split()))
n = int(n)
arr = [0]*n
arr[0] = a
right = a
left = 0

while right - left > 0.0001:
    check = True
    arr[1] = (left + right)/2
    for i in range(2, n):
        arr[i] = 2*arr[i - 1] - arr[i - 2] + 2
        if arr[i] < 0:
            check = False
            break
    if check:
        right = arr[1]
    else:
        left = arr[1]

print("%.2f" % arr[n - 1], file = fout)
fout.close()
