class PriorityQueue:
    def __init__(self):
        self.list = [[None]]  # Для выполнения условия родитель i, дети 2i и 2i + 1
        self.size = 0

    def sift_up(self, i):  # 0 for elem, 1 for line
        while i // 2 > 0:
            if self.list[i][0] < self.list[i // 2][0]:
                self.list[i // 2], self.list[i] = self.list[i], self.list[i // 2]
            i = i // 2

    def push(self, k):
        self.list.append(k)
        self.size += 1
        self.sift_up(self.size)

    def sift_down(self, i):
        while (i * 2) <= self.size:
            mc = self.min_child(i)
            if self.list[i][0] > self.list[mc][0]:
                self.list[i], self.list[mc] = self.list[mc], self.list[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.list[i*2][0] < self.list[i*2+1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def extract_min(self):  # Меняем первый и последний, делаем sift_down
        temp = self.list[1]
        self.list[1] = self.list[self.size]
        self.size = self.size - 1
        self.list.pop()
        self.sift_down(1)
        return temp[0]

    def decrease_key(self, line, key):
        for i in range(1, q.size + 1):
            if self.list[i][1] == line:
                if self.list[i][0] < key:
                    self.list[i][0] = key
                    self.sift_down(i)
                    break
                else:
                    self.list[i][0] = key
                    self.sift_up(i)
                    break

fin = open("priorityqueue.in")
fout = open("priorityqueue.out", "w")
line = fin.readline()

q = PriorityQueue()
count = 0

'''
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.pop())
print(q.extract_min())
print(q.pop())
print(q.extract_min())
'''

'''
q.push([1,1])
q.push([2,2])
q.push([7,3])
q.push([1,4])
q.push([8,5])
q.push([9,6])
q.push([3,7])
print(q.extract_min())
q.decrease_key(4, 3)
print(q.extract_min())
'''

while line != '':
    count += 1
    if line[0] == 'p':  # for push
        q.push([int(line[5:-1]), count])
    elif line[0] == 'e':  # extract-min
        if q.size == 0:
            print('*', file = fout)
        else:
            print(q.extract_min(), file = fout)
    else:
        a = line.split()
        q.decrease_key(int(a[1]), int(a[2]))
    line = fin.readline()

fout.close()
