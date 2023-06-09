---
fixme: true
id: 5a78b4a6-c2b4-4b65-a01a-12e8958d5a18
longname: Максимум суммы ключей дерева
tags: [btree]
languages: [python]
checker: cmp_long_long
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Рассмотрим двоичное дерево поиска. Для данного двоичного дерева найдите максимально возможную сумму ключей на пути от корня к листу. Ключи корня и листа также входят в эту сумму.

Задачу требуется решить за время O(N), N - количество вершин.

### Формат входных данных

На вход программа получает двоичное дерево в следующем формате:
В первой строке одно число n - количество вершин (1 <= n <= 1000). В следующих n строках описания вершин, каждое в виде трех числе через пробел: value, left, right, где value - значение в текущей вершине, left и right - номера ее левого и правого потомков. Если потомка нет то соответствующее значение будет -1. Вершины нумеруются с нуля, нулевая вершина - это корень дерева.

### Формат выходных данных

Выведете одно число - максимальную сумму ключей на пути от корня к листу.

### Примеры

```
-> 3
-> 5 -1 1
-> 15 -1 2
-> 18 -1 -1
--
<- 38
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
<- 99
```
