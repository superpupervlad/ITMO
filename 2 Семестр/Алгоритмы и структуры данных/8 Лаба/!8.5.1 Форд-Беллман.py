import sys
fin = open("pathbge1.in")
fout = open("pathbge1.out", "w")

# n - Количетсво вершин  m - Количество ребер
inf = sys.maxsize
n, m = list(map(int, fin.readline().split()))
distance = [inf for _ in range(n)]
distance[0] = 0
inf = inf
edges = []
t = [None, None]
for i in range(m):
    temp = list(map(int, fin.readline().split()))
    temp[0] -= 1
    temp[1] -= 1
    edges.append(temp.copy())
    t[0] = temp[1]
    t[1] = temp[0]
    edges.append(t.copy())

for i in range(n):
    check = False
    for j in range(2*m):
        if distance[edges[j][1]] > distance[edges[j][0]] + 1:
            distance[edges[j][1]] = distance[edges[j][0]] + 1
            check = True
    if not check:
        break
print(edges)
for _ in range(n):
    print(distance[_], end=' ', file=fout)

fout.close()