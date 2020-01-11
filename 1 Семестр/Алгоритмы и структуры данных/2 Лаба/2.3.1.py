def sort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        middle = (len(arr) // 2)
        left, count_left = sort(arr[:middle])
        right, count_right = sort(arr[middle:])
        result, count_result = merge(left, right)
        return result, (count_left + count_right + count_result)


def merge(a, b):
    result = []
    count = 0
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            result.append(a[0])
            a.remove(a[0])
        else:
            result.append(b[0])
            b.remove(b[0])
            count += len(a)
    if len(a) == 0:
        result = result + b
    else:
        result = result + a
    return result, count


fin = open("inversions.in")
fout = open("inversions.out", "w")
n = map(int, fin.readline().split())
array = list(map(int, fin.readline().split()))
array, count = sort(array)
print(count, file = fout)
fout.close()