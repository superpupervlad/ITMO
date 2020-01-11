def sort(Country, index):
    if len(Country) > 1:
        mid = len(Country) // 2
        L = Country[:mid]
        R = Country[mid:]

        sort(L, index)
        sort(R, index)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][index - 1] <= R[j][index - 1]:
                Country[k] = L[i]
                i += 1
            else:
                Country[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            Country[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            Country[k] = R[j]
            j += 1
            k += 1


fin = open("radixsort.in")
fout = open("radixsort.out", "w")
task = list(map(int, fin.readline().split()))
arr = []
for i in range(task[0]):
    arr.append(fin.readline()[0:task[1]])
for j in range(task[1], task[1] - task[2], -1):
    sort(arr, j)
for elem in arr:
    print(elem, file = fout)
fout.close()
