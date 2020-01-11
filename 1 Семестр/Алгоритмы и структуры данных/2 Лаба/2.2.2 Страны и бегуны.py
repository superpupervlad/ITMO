def sort(Country):
    if len(Country) > 1:
        mid = len(Country) // 2
        L = Country[:mid]
        R = Country[mid:]

        sort(L)
        sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][0] <= R[j][0]:
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


fin = open("race.in")
fout = open("race.out", "w")
n = int(fin.readline())
Country = []
for i in range(n):
    x = list(map(str, fin.readline().split()))
    Country.append(x)
sort(Country)
current = Country[0][0]
i = 0
while i < len(Country):
    current = Country[i][0]
    print('=== ' + Country[i][0] + ' ===', file = fout)
    while current == Country[i][0]:
        print(Country[i][1], file = fout)
        i += 1
        if i >= len(Country):
            break
fout.close()