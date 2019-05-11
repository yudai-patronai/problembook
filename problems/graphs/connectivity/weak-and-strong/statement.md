---
fixme: true
id: de2efbda-7f5f-4d9f-b59a-1284d7b949f6
longname: Сильные и слабые компоненты связности
tags: [graphs, connectivity, dfs]
languages: [python]
checker: cmp_int_seq
time_limit: 4
real_time_limit: 10
max_vm_size: 256M
---

Ориентированный граф задан в формате списка рёбер. Нужно посчитать количество слабых и сильных компонент связности.

### ### Формат входных данных

В первой строке вводится количество вершин N (0 <= N <= 10^3). Вершины без названий, их номера — 0, 1, 2 и т.д. до (N-1)-й включительно.

Во второй строке вводится количество рёбер M (0 <= M <= 10^5). Затем вводится M строк, содержащих по два числа через пробел — это номера вершин, задающих ребро графа. Рёбра **направленные**.

### ### Формат выходных данных

Количество слабых и количество сильных компонент связности

### Примеры

```
-> 3
-> 3
-> 1 2
-> 2 0
-> 0 1
--
<- 1 1
```

```
-> 4
-> 4
-> 0 1
-> 1 2
-> 2 3
-> 1 0
--
<- 1 3
```

```
-> 5
-> 6
-> 1 2
-> 2 3
-> 3 2
-> 2 1
-> 4 1
-> 2 0
--
<- 1 3
```