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


fin = open("brackets.in")
fout = open("brackets.out", "w")

s_open = Stack()
s_close = Stack()

line = fin.readline()

while line != "":
    for bracket in line[:-1]:
        if bracket == "[" or bracket == "(":
            s_open.push(bracket)
        else:
            if s_open.isEmpty():
                print("NO", file=fout)
                check = 1
                break
            else:
                if bracket == "]":
                    if s_open.pop() == "(":
                        print('NO', file=fout)
                        check = 1
                        break
                else:
                    if s_open.pop() == "[":
                        print('NO', file=fout)
                        check = 1
                        break
    else:  # Не случилось ли break
        if s_open.isEmpty() and s_close.isEmpty():
            print("YES", file=fout)
        else:
            print('NO', file=fout)
    s_open = Stack()  # Очистка
    s_close = Stack()
    line = fin.readline()


fout.close()
