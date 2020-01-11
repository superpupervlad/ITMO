from math import sqrt


def hash_function(self, value):
    #return int(self.size * ((value * CONST_NAME)%1))
    return value % self.size


class HashTable:
    def __init__(self, size=100000):
        self.size = size
        self.table = [List() for _ in range(self.size)]
        self.count = 0

    def put(self, data):
        if not self.exist(data):
            self.table[hash(data) % self.size].push(data)
            self.count += 1

    def exist(self, data):
        elem = self.table[hash(data) % self.size].head
        if elem is None:
            return False
        while elem.next and elem.data != data:
            elem = elem.next
        return elem.data == data

    def delete_element(self, data):
        elem = self.table[hash(data) % self.size].head
        pastelem = elem
        if elem is not None:
            if self.table[hash(data) % self.size].head == self.table[hash(data) % self.size].tail and elem.data == data:  # Только один нужный эл. в списке
                self.table[hash(data) % self.size].head = None
                self.table[hash(data) % self.size].tail = None
            else:
                return
        else:
            return
        while elem.next and elem.data != data:  # Находим последний эл. (пока ссылка на след. эл. не None)
            pastelem = elem
            elem = elem.next
        if elem.data == data and pastelem != elem:
            pastelem.next = elem.next
        elif self.table[hash(data) % self.size].head == self.table[hash(data) % self.size].tail:  # Только один нужный эл. в списке
            self.table[hash(data) % self.size].head = None
            self.table[hash(data) % self.size].tail = None
        elif pastelem == elem:
            self.table[hash(data) % self.size].head = elem.next


class Element:
    def __init__(self, data=None, exist=0):  # Если не передали значения, то data == None
        self.data = data
        self.next = None
        self.exist = exist


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        newelement = Element(data)
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


fin = open("set.in")
fout = open("set.out", "w")

CONST_NAME = 0.923847

HashTable.hsh = hash_function

line = fin.readline()
h = HashTable()

while line != "":
    if line[0] == "i":
        h.put(int(line[7:-1]))
    elif line[0] == "e":
        if h.exist(int(line[7:-1])):
            print('true', file=fout)
        else:
            print('false', file=fout)
    else:
        h.delete_element(int(line[7:-1]))
    line = fin.readline()

fout.close()
