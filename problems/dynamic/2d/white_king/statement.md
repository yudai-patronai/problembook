---
id: 982d3c81-9848-4d21-ae2e-6cb98ccb00c8
longname: Белый король
languages: [python]
tags: [dynamic, io, chess]
checker: cmp_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

На шахматной доске стоят белый король и черный конь. Конь неподвижен, король может ходить на одну клетку вправо, на одну клетку вверх или наискосок вправо-вверх. Посчитайте, сколькими способами король может дойти до клетки h8, начав с клетки a1. Королю нельзя попадать под атаку коня. Самого коня есть тоже нельзя.

Строки шахматной доски пронумерованы числами от 1 до 8, столбцы буквами от a до h. Строка 1 - самая нижняя, столбец a - самый левый.

### Формат входных данных

В единственной строке - позиция коня. Позиция - это два символа, буква столбца и номер строки, например a3.

### Формат выходных данных

Одно число — результат.

### Примеры

```
-> b2
--
<- 4932
```

```
-> e5
--
<- 1072
```
