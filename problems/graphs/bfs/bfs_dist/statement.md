---
id: b2380a9a-697f-4a43-914d-808be407ead0
longname: Поиск кратчайшего пути между двумя вершинами невзвешенного графа
tags: [graphs,bfs]
languages: [python]
checker: cmp_int
time_limit: 1
real_time_limit: 5
max_vm_size: 64M
---

Дан невзвешенный связный неориентированный граф. Вершины пронумерованы от 0. Трeбуется с помощью обхода в ширину найти расстояние от начальной вершины до конечной.

### Формат входных данных

Первая строка содержит четыре числа через пробел `N M S F`:

- `N` - количество вершин в графе, `2 ≤ N ≤ 1000`;
- `M` - количество рёбер в графе, `1 ≤ M ≤ 20000`;
- `S` - начальная вершина;
- `F` - конечная вершина.

В следующих `M` строках задаются рёбра графа, по два числа в каждой строке - номера соединенных вершин.

### Формат выходных данных

Требуется распечатать одно число - расстояние от вершины `S` до вершины `F`.

### Примеры

```
-> 2 1 0 1
-> 0 1
--
<- 1
```

```
-> 8 10 5 2
-> 4 7
-> 5 1
-> 0 1
-> 3 1
-> 0 2
-> 3 5
-> 3 4
-> 0 4
-> 4 6
-> 5 4
--
<- 3
```
