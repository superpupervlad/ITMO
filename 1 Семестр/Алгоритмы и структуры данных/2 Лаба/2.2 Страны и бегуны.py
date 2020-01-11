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
        quick_sort(q_array, low, indexx)  # left
        quick_sort(q_array, indexx + 1, high)  # right


fin = open("race.in")
fout = open("race.out", "w")
n = int(fin.readline())
Names = dict()

for i in range(n):
    x = list(map(str, fin.readline().split()))
    if x[0] not in Names:
        Names[x[0]] = []
    Names[x[0]].append(x[1])
Names_list = list(Names.keys())
quick_sort(Names_list, 0, len(Names_list) - 1)
print(Names_list)
for country in Names_list:
    print('=== ' + country + ' ===', file=fout)
    for name in Names[country]:
        print(name, file=fout)

fout.close()
