def make_heap():
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, i, n)


def heapify(arr, i, n):
    high = i
    left = 2*i + 1
    right = left + 1
    if left < n:
        if arr[high] < arr[left]:
            high = left
        if right < n:
            if arr[high] < arr[right]:
                high = right
    if high != i:
        arr[i], arr[high] = arr[high], arr[i]
        heapify(arr, high, n)  # для того эл. который мы поменяли


def heap_sort(arr, n):
    for i in range(n):
        new.append(arr[0])
        arr[0], arr[-1] = arr[-1], arr[0]
        del arr[-1]
        heapify(arr, 0, len(arr))


fin = open("sort.in")
fout = open("sort.out", "w")
new = []
n = int(fin.readline())
arr = list(map(int, fin.readline().split()))
make_heap()
heap_sort(arr, len(arr))
for i in range(len(new) - 1, -1, -1):
    print(new[i], end = ' ', file = fout)
fout.close()
