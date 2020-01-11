import sys
sys.setrecursionlimit(10 ** 9)

def find(ind, current_height):
    if tree[ind] is None:
        return current_height
    else:
        a = find(tree[ind][1], current_height + 1)
        b = find(tree[ind][2], current_height + 1)
        out[ind - 1] = b - a
        return max(a, b)


fin = open("balance.in")
fout = open("balance.out", "w")

n = int(fin.readline())
tree = [None]
possible_heads = {i for i in range(1, n + 1)}

for i in range(n):
    temp = list(map(int, fin.readline().split()))
    tree.append(temp)
    possible_heads.discard(temp[1])
    possible_heads.discard(temp[2])

out = [0] * n

if n < 1:
    print(0, file=fout)
else:
    find(1, 0)
    for elem in out:
        print(elem, file=fout)

fout.close()
