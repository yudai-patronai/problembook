---
id: 61a9faff-b621-40ca-853f-49dfad2a8d67
longname: Сортировка выбором — рекурсивный вариант
languages: [python]
tags: [sort,recursion]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Написать программу, осуществляющую сортировку выбором введённых целых чисел по возрастанию c использованием рекурсии.
**Внимание! Сначала необходимо считать все введённые числа в один список**

Использование конструкций `sort` и `sorted` запрещено!

### Формат входных данных

Последовательность целых чисел, разделённая символом пробел.

### Формат выходных данных

Набор расстановок чисел в сортируемом массиве.
**Внимание! Надо выводить весь массив после КАЖДОЙ перестановки элементов в нём. Если перестановки
на какой-либо итерации не было — НИЧЕГО не выводить**

### Примеры

```
-> 3 2 1
--
<- 1 2 3
```

```
-> 1 2
--
<- &#32;
```