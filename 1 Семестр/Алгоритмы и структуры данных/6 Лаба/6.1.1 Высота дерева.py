class BinaryTree:
    def __init__(self, size, head=None):
        self.size = size
        self.table = [[] for _ in range(self.size + 1)]
        self.table[0] = None
        self.head = head

    def add(self, element, index):
        self.table[index] = element


class Node:
    def __init__(self, data, left, right, height=0):
        self.data = data
        self.left = BT.table[left]
        self.right = BT.table[right]
        self.height = height


fin = open("height.in")
fout = open("height.out", "w")

n = int(fin.readline())
BT = BinaryTree(n)
possible_heads = {i for i in range(1, n + 1)}
temp_file = [None]
for i in range(1, n + 1):
    t = fin.readline()
    temp = list(map(int, t.split()))
    new = Node(temp[0], temp[1], temp[2])
    BT.add(new, i)
    possible_heads.discard(temp[1])
    possible_heads.discard(temp[2])
    temp_file.append(t)
for i in range(1, n + 1):
    temp = list(map(int, temp_file[i].split()))
    new = Node(temp[0], temp[1], temp[2]) # Попытаться просто переопределить детей без замены эл.
    BT.add(new, i)
    possible_heads.discard(temp[1])
    possible_heads.discard(temp[2])

BT.head = BT.table[possible_heads.pop()]
BT.head.height = 1

height = []
height.append(BT.head)
m = 0

while height != []:
    left = height[-1].left
    height.append(left)
    if left is not None:
        left.height = height[-1].height + 1
        continue
    else:
        if height[-1] is not None:
            m = max(m, height[-1].height)
        height.pop()
    right = height[-1].right
    height.append(right)
    if right is not None:
        right.height = height[-2].height + 1
        continue
    else:
        if height[-1] is not None:
            m = max(m, height[-1].height)
        height.pop()
print(m)
fout.close()
