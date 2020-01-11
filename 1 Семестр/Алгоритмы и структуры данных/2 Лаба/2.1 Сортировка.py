import random

def partition(p_array, low, high):
    pivot = p_array[random.randint(low, high)]
    left = low - 1
    right = high + 1
    while True:
        left += 1
        while p_array[left] < pivot:
            left += 1

        right -= 1
        while p_array[right] > pivot:
            right -= 1

        if left >= right:
            return right

        p_array[left], p_array[right] = p_array[right], p_array[left]

def quick_sort(q_array, low, high):
    if low < high:
        indexx = partition(q_array, low, high)
        quick_sort(q_array, low, indexx)#left
        quick_sort(q_array, indexx + 1, high)#right

fin = open("sort.in")
fout = open("sort.out", "w")
n = map(int, fin.readline().split())
array = list(map(int, fin.readline().split()))
quick_sort(array,0,len(array) - 1)
for i in range(len(array)):
    print(array[i],end = ' ',file=fout)
fout.close()