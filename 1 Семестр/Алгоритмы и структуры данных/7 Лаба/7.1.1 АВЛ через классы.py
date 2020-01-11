class Node:
    def __init__(self, key, left, right):
        self.children = [left, right]
        self.height = 0
        self.key = key


class AVL_Tree:
    def __init__(self, size):
        self.table = [None] * size

    def balance(self, v):
        if self.table[v].children[1] != -1:
            a = self.table[self.table[v].children[1]].height
        else:
            a = 0
        if self.table[v].children[0] != -1:
            b = self.table[self.table[v].children[0]].height
        else:
            b = 0
        return a - b

    def count_height(self):
        self.dfs(self.table[0])

    def height_right(self, v):
        return 0 if v.children[1] == -1 else self.table[v.children[1]].height

    def height_left(self, v):
        return 0 if v.children[0] == -1 else self.table[v.children[0]].height

    def dfs(self, v):
        for child in v.children:
            if child != -1:
                self.dfs(self.table[child])
        v.height = max(self.height_left(v), self.height_right(v)) + 1


fin = open("balance.in")
fout = open("balance.out", "w")

n = int(fin.readline())
avl = AVL_Tree(n)

for i in range(n):
    key, left, right = list(map(int, fin.readline().split()))
    avl.table[i] = Node(key, left - 1, right - 1)

avl.count_height()
for i in range(n):
    print(avl.balance(i), file = fout)
fout.close()
