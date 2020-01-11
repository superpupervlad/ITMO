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


fin = open("postfix.in")
fout = open("postfix.out", "w")

s = Stack()

string = fin.readline()[:-1]
string = string.replace(' ', '')

for elem in string:
    if elem == '+':
        s.push(s.pop()+s.pop())
    elif elem == '-':
        temp = s.pop()
        s.push(s.pop()-temp)
    elif elem == '*':
        s.push(s.pop()*s.pop())
    else:
        s.push(int(elem))
print(s.pop(), file=fout)

fout.close()
