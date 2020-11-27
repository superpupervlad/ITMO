def khun(ver):
    if used[ver]:
        return False
    used[ver] = True
    for i in range(len(graph[ver])):
        to = graph[ver][i]
        if match[to] is None or khun(match[to]):
            match[to] = ver
            return True
    return False


fin = open("matching.in")
fout = open("matching.out", "w")

n1, n2, m = list(map(int, fin.readline().split()))

graph = [[] for _ in range(n1)]
match = [None for _ in range(n2)]

for i in range(m):
    a, b = list(map(int, fin.readline().split()))
    graph[a - 1].append(b - 1)

for i in range(n1):
    used = [None] * n1
    khun(i)

res = 0
for i in range(n2):
    if match[i] is not None:
        res += 1
print(res, file = fout)
