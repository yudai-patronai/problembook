---
id: cb14889c-324f-48ae-8f0b-e217e4dc414a
longname: Задача о китайском почтальоне
tags: [graphs]
time_limit: 4
real_time_limit: 4
max_vm_size: 64M
---


Дан неориентированный взвешенный связный граф. Найти вес минимального цикла проходящего через каждое ребро графа хотябы один раз.

### Формат входных данных

На вход программе в первой строке подаются через пробел два числа: `N` (2 <= `N` <= 100) - число вершин в графе и `M` (1 <= `M` <= 5000) - число ребер. В следующих `M` строках задаются ребра, по три числа в каждой строке - номера соединенных вершин и вес ребра.

### Формат выходных данных

Одно число — вес искомого цикла.

### Примеры
```
-> 2 1
-> 0 1 12
--
<- 24
```

```
-> 6 6
-> 3 2 36
-> 1 0 53
-> 1 2 34
-> 1 5 3
-> 3 4 3
-> 5 3 64
--
<- 249
```