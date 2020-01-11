def hash_function(self, value):
    t = 139
    for char in value:
        t = t*31 + ord(char)
    return t % self.size


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def put(self, data):
        check = self.where(data[0])
        hhh = self.hsh(data[0])
        if check is not None:
            self.table[hhh][check][1] = data[1]
            return self.table[hhh][check], 0
        else:
            self.table[hhh].append(data)
            return self.table[hhh][-1], 1

    def where(self, data):
        index = self.hsh(data)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == data:
                return i
        return None

    def edit_next(self, prev_elem, next_elem):  # Изменяет next у prev эл.
        if prev_elem is not None:
            prev_elem[3] = next_elem

    def edit_prev(self, next_elem, prev_elem):
        if next_elem is not None:
            next_elem[2] = prev_elem

    def delete_element(self, data):
        self.edit_next(data[2], data[3])
        self.edit_prev(data[3], data[2])
        del self.table[self.hsh(data[0])][self.where(data[0])]


fin = open("linkedmap.in")
fout = open("linkedmap.out", "w")

HashTable.hsh = hash_function

line = fin.readline().split()
h = HashTable()
prev = None
# Сделать prev и next ссылками на объект
while line:
    if line[0] == "put":
        zip_element = [None]*4  # 0 key, 1 - value, 2 - prev, 3 - next
        zip_element[0] = line[1]
        zip_element[1] = line[2]
        if prev is not None:
            if line[0] != prev[0]:
                zip_element[2] = prev
        new_element = h.put(zip_element)
        if new_element[1] == 1:
            h.edit_next(prev, new_element[0])
        if new_element[1] == 1:
            prev = new_element[0]

    elif line[0] == "get":
        temp = h.where(line[1])
        if temp is not None:
            print(h.table[h.hsh(line[1])][temp][1], file=fout)
        else:
            print("none", file=fout)

    elif line[0] == "prev":
        check = h.hsh(line[1])
        check2 = h.where(line[1])
        if check is not None and check2 is not None:
            temp = h.table[check][check2][2]
            if temp is not None:
                print(temp[1], file=fout)
            else:
                print("none", file=fout)
        else:
            print("none", file=fout)

    elif line[0] == "next":
        check = h.hsh(line[1])
        check2 = h.where(line[1])
        if check is not None and check2 is not None:
            temp = h.table[check][check2][3]
            if temp is not None:
                print(temp[1], file=fout)
            else:
                print("none", file=fout)
        else:
            print("none", file=fout)

    else:
        check = h.hsh(line[1])
        check2 = h.where(line[1])
        if check is not None and check2 is not None:
            if prev == h.table[check][check2]:
                prev = h.table[check][check2][2]
            h.delete_element(h.table[check][check2])
    line = fin.readline().split()

fout.close()
