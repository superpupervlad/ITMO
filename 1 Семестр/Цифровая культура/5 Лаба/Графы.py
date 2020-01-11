import networkx as nx
#import matplotlib.pyplot as plt
graph_edges = open('graphedges61.txt')


def find_de_way(graph, a, b):
    print('Найти путь от ' + str(a) + ' до ' + str(b))
    path = nx.shortest_path(graph, a, b)
    print('Длина: ' + str(len(path)))
    print('Путь: ' + str(path[0]), end='')
    for i in range(1, len(path)):
        print(' -> ', end='')
        print(str(path[i]), end='')
    print()


print('-----Тупа подготовка-----')
original_graph = list()
set_graph = set()
dic_graph = dict()
g = nx.Graph()

for line in graph_edges:
    original_graph.append(list(map(int, line.split())))

for node in original_graph:
    set_graph.add(node[0])
    set_graph.add(node[1])

    for i in range(2):
        if node[i] not in dic_graph:
            dic_graph[node[i]] = 1
        else:
            dic_graph[node[i]] += 1

    g.add_edge(node[0], node[1])

print('Нормас подготовились')
print('-----Тупа подготовка-----\n')

print('\n1 ВОПРОС')
print('Всего ребер: ' + str(len(original_graph)))

print('\n2 ВОПРОС')
isolated = sorted(list({i for i in range(1000)} - set_graph))
print('Всего изолятов: ' + str(len(isolated)))
print('Сами изоляты: ', end='')
for isolate in isolated:
    print(isolate, end=', ')
print()

print('\n3 ВОПРОС')
maximum = 0
t_node = 'Нет такого графа'
t_value = 'Никакая'
for i in set_graph:
    if dic_graph.get(i) > maximum:
        t_node = i
        t_value = dic_graph[i]
        maximum = t_value

print('Вершина с самой большой степенью - ' + str(t_node) + '. Степень связности - ' + str(t_value) + '.')

print('\n4 ВОПРОС')
all_subgraphs = []
maximum = -1
for component in list(nx.connected_components(g)):
    temp = g.subgraph(node for node in component)
    all_subgraphs.append(temp)  # Все компоненты нашего графа
for component in all_subgraphs:
    print('...')
    t = nx.diameter(component)
    if t > maximum:
        maximum = t
print('Диаметр компоненты связности: ' + str(maximum))

print('\n5 ВОПРОС')
find_de_way(g, 807, 216)

print('\n6 ВОПРОС')
find_de_way(g, 463, 908)

print('\n7 ВОПРОС')
find_de_way(g, 817, 37)

print('\n---УДАЛЕНИЕ---')
for node in original_graph:
    for i in range(2):
        if (node[i] == 193 or node[i] == 903 or node[i] == 72 or node[i] == 266 or
        node[i] == 139 or node[i] == 154 or node[i] == 155 or node[i] == 796 or
        node[i] % 17 == 0):
                original_graph.remove(node)
                break

print('\n-----Тупа подготовка-----')
set_graph = set()
dic_graph = dict()
g = nx.Graph()

for line in graph_edges:
    original_graph.append(list(map(int, line.split())))

for node in original_graph:
    set_graph.add(node[0])
    set_graph.add(node[1])

    for i in range(2):
        if node[i] not in dic_graph:
            dic_graph[node[i]] = 1
        else:
            dic_graph[node[i]] += 1

    g.add_edge(node[0], node[1])

print('Нормас подготовились')
print('-----Тупа подготовка-----\n')

print('\n8 ВОПРОС')
print('Всего ребер: ' + str(len(original_graph)))

print('\n9 ВОПРОС')
isolated = sorted(list({i for i in range(1000)} - set_graph))
print('Всего изолятов: ' + str(len(isolated)))
print('Сами изоляты: ', end='')
for isolate in isolated:
    print(isolate, end=', ')
print()

print('\n10 ВОПРОС')
maximum = 0
t_node = 'Нет такого графа'
t_value = 'Никакая'
for i in set_graph:
    if dic_graph.get(i) > maximum:
        t_node = i
        t_value = dic_graph[i]
        maximum = t_value

print('Граф - ' + str(t_node) + '. Степень связности - ' + str(t_value) + '.')

print('\n11 ВОПРОС')
all_subgraphs = []
maximum = -1
for component in list(nx.connected_components(g)):
    temp = g.subgraph(node for node in component)
    all_subgraphs.append(temp)  # Все компоненты нашего графа
for component in all_subgraphs:
    print('...')
    t = nx.diameter(component)
    if t > maximum:
        maximum = t
print('Диаметр компоненты связности: ' + str(maximum))

print('\n12 ВОПРОС')
find_de_way(g, 807, 216)

print('\n13 ВОПРОС')
find_de_way(g, 463, 908)

print('\n14 ВОПРОС')
find_de_way(g, 817, 37)

#nx.draw(g)
#plt.show()
