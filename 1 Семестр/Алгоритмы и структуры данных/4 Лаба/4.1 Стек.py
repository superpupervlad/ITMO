class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):  # Пустой ли стек
        return self.items == []

    def push(self, item):  # Добавляем элемент
        self.items.append(item)

    def pop(self):  # Берем верхний и удаляем его
        return self.items.pop()

    def peek(self):  # Берем верхний без удаления
        return self.items[len(self.items) - 1]

    def size(self):  # Размер стека
        return len(self.items)


fin = open("stack.in")
fout = open("stack.out", "w")

s = Stack()

for i in range(int(fin.readline())):
    line = fin.readline()
    if line[0] == "+":
        s.push(line[2:-1])
    else:
        print(s.pop(), file=fout)

fout.close()
