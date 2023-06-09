---
id: f675123f-66e3-4873-80ca-95fd3e190ad5
longname: Алгоритм Форда-Беллмана
languages: [python,cpp]
tags: [graphs,ford_bellman]
checker: cmp_file
time_limit: 1
real_time_limit: 2
max_vm_size: 64M
---

Дан ориентированный взвешенный граф и номер стартовой вершины.
Вершины нумеруются с нуля.
Необходимо определить кратчашие расстояния от неё до остальных вершин.

### Формат входных данных

На вход программе в первой строке подается три числа через пробел: `n`, `m`, `s`. 

- 2 ≤ `n` ≤ 1000 - число вершин в графе
- 1 ≤ `m` ≤ 1000 - число рёбер
- `s` - номер начальной вершины

В следующих `m` строках задаются рёбра.
Ребро (дуга) задаётся тремя числами через пробел:

1. Начало ребра
2. Конец ребра
3. Вес ребра

Вес ребра - целое число, по модулю не превышаюшее 1000.

### Формат выходных данных

Необходимо вывести строку из n элементов через пробел - расстояния до вершин из заданной.
Если расстояние до какой-то вершины не определено, то выведите вместо этого расстояния строку `UDF`.

### Примеры

```
-> 2 1 0
-> 0 1 5
--
<- 0 5
```

```
-> 4 5 0
-> 0 1 10
-> 0 2 40
-> 1 2 15
-> 0 3 20
-> 3 1 5
--
<- 0 10 25 20
```
