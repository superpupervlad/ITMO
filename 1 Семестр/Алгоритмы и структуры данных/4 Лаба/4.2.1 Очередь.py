class element:
    def __init__(self, data=None):  # Если не передали значения, то data == None
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        newelement = element(data)
        if self.head is None:
            self.tail = newelement
            self.head = newelement
        else:
            prevelement = self.tail
            prevelement.next = newelement
            self.tail = newelement

    def pop(self):
        temp = self.head
        self.head = temp.next
        return temp.data

    def peek(self):
        temp = self.head
        return temp.data


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
