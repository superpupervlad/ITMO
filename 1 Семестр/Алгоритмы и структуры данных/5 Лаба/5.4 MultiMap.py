def hash_function(self, value):
    return abs(hash(value)) % self.size


def hash_function2(self, value):
    h = 293
    for char in value:
        h = h * 89 + ord(char)
    return h % self.size


class SmallHashTable:
    def __init__(self, size=2):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.real_size = 0

    def put(self, data):
        if not self.exist(data):
            temp = self.hsh(data)
            self.table[temp].append(data)
            self.real_size += 1

    def exist(self, data):
        return data in self.table[self.hsh(data)]

    def delete_element(self, data):
        if data in self.table[self.hsh(data)]:
            self.table[self.hsh(data)].remove(data)
            self.real_size -= 1
        else:
            return


class HashTable:
    def __init__(self, size=2):
        self.size = size
        self.table = [[[]] for _ in range(self.size)]

    def put(self, data):
        check = self.where(data[0])
        check2 = self.hsh(data[0])
        if check is not None:
            self.table[check2][check][1].put(data[1])
        else:
            self.table[check2].append([None, SmallHashTable()])
            self.table[check2][-1][0] = data[0]
            self.table[check2][-1][1].put(data[1])

    def where(self, data):
        index = self.hsh(data)
        for i in range(len(self.table[index])):
            if self.table[index][i]:
                if self.table[index][i][0] == data:
                    return i
        return None

    def delete_one(self, data):
        check = self.where(data[0])
        check2 = self.hsh(data[0])
        if check is not None:
            self.table[check2][check][1].delete_element(data[1])

    def delete_all(self, data):
        check = self.where(data)
        if check is not None:
            self.table[self.hsh(data)][check] = [None, SmallHashTable()]


fin = open("multimap.in")
fout = open("multimap.out", "w")

HashTable.hsh = hash_function
SmallHashTable.hsh = hash_function2

line = fin.readline().split()
h = HashTable()

while line:
    if line[0] == "put":
        h.put(line[1:])

    elif line[0] == "get":
        check = h.where(line[1])
        check2 = h.hsh(line[1])
        if check is not None and h.table[check2][check][1].real_size > 0:
            print(h.table[check2][check][1].real_size, file=fout, end=' ')
            for i in range(h.table[check2][check][1].size):
                if h.table[check2][check][1].table[i]:
                    for elem in h.table[check2][check][1].table[i]:
                        print(elem, file=fout, end=' ')
            print(file=fout)
        else:
            print(0, file=fout)

    elif line[0] == "delete":
        h.delete_one(line[1:])

    else:
        h.delete_all(line[1])

    line = fin.readline().split()

fout.close()
