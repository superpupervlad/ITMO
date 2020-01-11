def hash_function(self, value):
    h = 29387
    for char in value:
        h = h*89 + ord(char)
    return h % self.size


class HashTable:
    def __init__(self, size=2):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def put(self, data):
        check = self.where(data[0])
        if check is not None:
            self.table[self.hsh(data[0])][check][1] = data[1]
        else:
            self.table[self.hsh(data[0])].append(data)

    def where(self, data):
        index = self.hsh(data)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == data:
                return i
        return None

    def delete_element(self, data):
        check = self.where(data)
        if check is not None:
            del self.table[self.hsh(data)][check]


fin = open("map.in")
fout = open("map.out", "w")

HashTable.hsh = hash_function

line = fin.readline().split()
h = HashTable()

while line:
    if line[0] == "put":
        h.put(line[1:])
    elif line[0] == "get":
        temp = h.where(line[1])
        if temp is not None:
            print(h.table[h.hsh(line[1])][temp][1], file=fout)
        else:
            print("none", file=fout)
    else:
        h.delete_element(line[1])
    line = fin.readline().split()

fout.close()
