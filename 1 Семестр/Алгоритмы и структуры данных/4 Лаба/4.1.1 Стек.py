class element:
    def __init__(self, data=None):  # Если не передали значения, то data == None
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        newelement = element(data)
        newelement.next = self.head
        self.head = newelement

    def pop(self):
        temp = self.head
        self.head = temp.next
        return temp.data

    def peek(self):
        temp = self.head
        return temp.data


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
