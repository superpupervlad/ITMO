def merge(left, right):
    a = []
    l = r = 0
    max_l = len(left)
    max_r = len(right)
    while l < max_l and r < max_r:
        if left[l] <= right[r]:
            a.append(left[l])
            l += 1
        else:
            a.append(right[r])
            r += 1
            global count
            count += max_l - l

    if l < max_l:
        for z in range(l, max_l):
            a.append(left[z])
    if r < max_r:
        for y in range(r, max_r):
            a.append(right[y])
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
        if array[1] < array[0]:
            array[0], array[1] = array[1], array[0]
        return (array)

fin = open("inversions.in")
fout = open("inversions.out", "w")
count = 1
n = map(int, fin.readline().split())
array = list(map(int, fin.readline().split()))
array = sort(array)
print(count, file=fout)
fout.close()