class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):  # Пустая ли очередь
        return self.items == []

    def push(self, item):  # Добавляем элемент
        self.items.insert(0, item)

    def pop(self):  # Берем последний и удаляем его
        return self.items.pop()

    def peek(self):  # Берем последний без удаления
        return self.items[len(self.items) - 1]

    def size(self):  # Размер очереди
        return len(self.items)


fin = open("queue.in")
fout = open("queue.out", "w")

q = Queue()

for i in range(int(fin.readline())):
    line = fin.readline()
    if line[0] == "+":
        q.push(line[2:-1])
    else:
        print(q.pop(), file=fout)

fout.close()
