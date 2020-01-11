from sys import setrecursionlimit, maxsize
import threading

setrecursionlimit(10 ** 9)
threading.stack_size(67108864)


def main():
    def check(node, minimum, maximum):
        if node is None:
            return True
        elif node[0] >= maximum or node[0] <= minimum:
            return False
        else:
            return check(tree[node[1]], minimum, node[0]) and check(tree[node[2]], node[0], maximum)


    fin = open("check.in")
    fout = open("check.out", "w")

    n = int(fin.readline())
    tree = [None]
    m = 0
    possible_heads = {i for i in range(1, n + 1)}

    for i in range(n):
        temp = list(map(int, fin.readline().split()))
        tree.append(temp)
        possible_heads.discard(temp[1])
        possible_heads.discard(temp[2])

    if n < 1:
        print('YES', file=fout)
    else:
        head = possible_heads.pop()
        if check(tree[head], -maxsize, maxsize):
            print('YES', file=fout)
        else:
            print('NO', file=fout)

    fout.close()


thread = threading.Thread(target=main)
thread.start()
