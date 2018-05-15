from collections import OrderedDict

n, m = list(map(int, input().strip().split()))

connection = []
for _ in range(m):
    connection.append(list(map(int, input().strip().split())))
connectionf = []
for element in connection:
    if element not in connectionf:
        connectionf.append(element)

vertices = [[] for _ in range(n)]
for i, j in connectionf:
    vertices[i - 1].append(j - 1)

flag = True
out = []


def dfs(vertex):
    global flag
    color[vertex] = 'grey'
    for node in vertices[vertex]:
        if color[node] == 'white':
            dfs(node)
        if color[node] == 'grey':
            flag = False
    color[vertex] = 'black'
    out.append(vertex + 1)


color = OrderedDict((i, 'white') for i in range(n))
cycle = []
for key in color:
    steck = []
    if color[key] == 'white':
        dfs(key)

if flag:
    print('Yes')
else:
    print('No')
