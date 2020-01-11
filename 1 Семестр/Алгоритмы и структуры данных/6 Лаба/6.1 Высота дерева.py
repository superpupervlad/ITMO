import sys
sys.setrecursionlimit(200000)


def find(node, current_height):
    if node is None:
        return current_height
    else:
        return max(find(tree[node[1]], current_height + 1), find(tree[node[2]], current_height + 1))


fin = open("height.in")
fout = open("height.out", "w")

n = int(fin.readline())
tree = [None]
possible_heads = {i for i in range(1, n + 1)}

for i in range(n):
    temp = list(map(int, fin.readline().split()))
    tree.append(temp)
    possible_heads.discard(temp[1])
    possible_heads.discard(temp[2])

if n < 1:
    print(0, file=fout)
else:
    print(find(tree[possible_heads.pop()], 0), file=fout)

fout.close()
