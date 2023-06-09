---
id: 71d01452-637d-4971-b550-e21fa53adc3b
longname: Дисбаланс дерева поиска
tags: [graphs,binary,tree,btree]
languages: [python]
checker: cmp_long_long
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Назовем максимальныю разницу высот левого и правого поддерева для вершин двоичного дерева степенью дисбаланса дерева. Таким образом у сбалансированного дерева степень дисбаланса будет 0 или 1. Для данного двоичного дерева найдете степень его дисбаланаса.

Задачу требуется решить за время O(N), N - количество вершин.

### Формат входных данных

На вход программа получает двоичное дерево в следующем формате:
В первой строке одно число n - количество вершин (1 <= n <= 1000). В следующих n строках описания вершин, каждое в виде трех числе через пробел: value, left, right, где value - значение в текущей вершине, left и right - номера ее левого и правого потомков. Если потомка нет то соответствующее значение будет -1. Вершины нумеруются с нуля, нулевая вершина - это корень дерева.

### Формат выходных данных

Выведете одно число - степень дисбаланса дерева.

### Примеры

```
-> 3
-> 5 -1 1
-> 15 -1 2
-> 18 -1 -1
--
<- 2
```

```
-> 6
-> 12 1 2
-> 8 -1 -1
-> 26 3 4
-> 23 -1 -1
-> 28 -1 5
-> 33 -1 -1
--
<- 2
```
