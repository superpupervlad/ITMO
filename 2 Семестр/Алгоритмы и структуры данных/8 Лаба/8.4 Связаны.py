def dfs(vertice, number_of_connection):
    vertices[vertice][0] += 1
    vertices[vertice][1] = number_of_connection
    for i in range(len(matrix[vertice])):
        if vertices[matrix[vertice][i]][0] == 0:
            dfs(matrix[vertice][i], number_of_connection)
        else:
            if vertices[vertice][1] != vertices[matrix[vertice][i]][1]:
                normal_number_of_connections = vertices[matrix[vertice][i]][1]
                vertices[vertice][1] = normal_number_of_connections
                global count
                count -= 1
                dfs(matrix[vertice][i], normal_number_of_connections)


fin = open("components.in")
fout = open("components.out", "w")
# n - Количетсво вершин  m - Количество ребер
n, m = list(map(int, fin.readline().split()))
matrix = [[] for _ in range(n)]
count = 0
vertices = [[0, -1] for _ in range(n)]  # 0 не были 1 были
for i in range(m):
    t = list(map(int, fin.readline().split()))
    matrix[t[0] - 1].append(t[1] - 1)

matrix = tuple(matrix)

for i in range(n):
    count += 1
    dfs(i, count)

# print('matrix: ' + str(matrix) + '\nconnections: ' + str(connections) + '\nvertices: ' + str(vertices))
print(count, file=fout)
for elem in vertices:
    print(elem[1], end=' ', file=fout)
fout.close()