def bin_search_left(arr, right, x):
    left = 0
    count = 0
    while left < right:
        count += 1
        mid = (left + right)//2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
        if count == 100:
            break
    if arr[left] == x:
        print(left + 1, end=' ', file=fout)
    else:
        print("-1", end=' ', file=fout)


def bin_search_right(arr, right, x):
    left = 0
    if arr[-1] == x:
        print(len(arr), file=fout)
        return
    while left < right:
        mid = (left + right)//2
        if arr[mid] > x:
            right = mid
        else:
            left = mid + 1
    if arr[left - 1] == x:
        print(left, file=fout)
    else:
        print("-1", file=fout)


fin = open("binsearch.in")
fout = open("binsearch.out", "w")
n = map(int, fin.readline().split())
array = list(map(int, fin.readline().split()))
m = map(int, fin.readline().split())
elements = list(map(int, fin.readline().split()))
for elem in elements:
    bin_search_left(array, len(array) - 1, elem)
    bin_search_right(array, len(array) - 1, elem)
fout.close()
