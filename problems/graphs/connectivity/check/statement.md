---
id: 1f149524-be56-4cfb-82f1-acdae2be34aa
longname: Проверить связность графа
tags: [graphs, connectivity, dfs, bfs]
languages: [python, cpp]
checker: cmp_yesno
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

При помощи алгоритма обхода проверить, являетcя ли неориентированный граф связным.

*Граф является связным, если между любой парой его вершин существует маршрут.*


### Формат входных данных

В первой строке вводится количество вершин `N` в графе. Вершины нумеруются с нуля.

Во второй строке вводится количество рёбер `M` в графе.

Затем вводится `M` строк формата `u v`, где `u` и `v` номера вершин, образующих ребро.

### Формат выходных данных

Строка `YES`, если граф является связным, и строка `NO` в обратном случае.

### Примеры

```
-> 3
-> 3
-> 0 1
-> 1 2
-> 2 0
--
<- YES
```

```
-> 5
-> 3
-> 0 1
-> 1 2
-> 3 4
--
<- NO
```
