def merge(left, right):
    a = []
    while (len(left) * len(right) > 0):
        if left[0][0] <= right[0][0]:
            a.append(left[0])
            left.pop(0)
        else:
            a.append(right[0])
            right.pop(0)
    if (len(left) > 0):
        for i in range(len(left)):
            a.append(left[0])
            left.pop(0)
    if (len(right) > 0):
        for i in range(len(right)):
            a.append(right[0])
            right.pop(0)
    return a


def sort(array):
    if len(array) == 1:
        return array
    if len(array) > 2:
        left_array = array[:len(array) // 2]
        right_array = array[len(array) // 2:]
        left_array = sort(left_array)
        right_array = sort(right_array)
        return (merge(left_array, right_array))
    if len(array) == 2:
        if array[1][0] < array[0][0]:
            array[0], array[1] = array[1], array[0]
        return (array)


fin = open("race.in")
fout = open("race.out", "w")
n = int(fin.readline())
Country = []
for i in range(n):
    x = list(map(str, fin.readline().split()))
    Country.append(x)
Country = sort(Country)
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
