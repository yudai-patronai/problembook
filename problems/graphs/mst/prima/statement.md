---
id: fbd7fd6f-17da-4aed-b37f-a0146d242b6d
longname: Минимальное остовное дерево (Алгоритм Прима)
tags: [graphs,prima]
languages: [python]
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Дан взвешенный неориентированный связный граф. Вершины пронумерованы от 0. Требуется найти минимальный вес остовного дерева графа и соответствующее ему остовное дерево.

### Формат входных данных

На вход программе в первой строке подаются через пробел два числа:

- `N` (2 <= `N` <= 1000) - число вершин в графе;
- `M` (1 <= `M` <= 20000) - число рёбер.

В следующих `M` строках задаются рёбра, по три числа в каждой строке - номера соединенных вершин и вес ребра.

### Формат выходных данных

На первой строке одно число - суммарный вес минимального остовного дерева. Дальше требуется распечатать N-1 пару чисел, каждyю на новой строке. Каждая пара задаёт ребро в минимальном остовном дереве.

### Примеры
```
-> 2 1
-> 1 0 5
--
<- 5
<- 0 1
```

```
-> 4 5
-> 0 1 10
-> 0 2 40
-> 1 2 15
-> 0 3 20
-> 3 1 5
--
<- 30
<- 0 1
<- 1 2
<- 1 3
```
