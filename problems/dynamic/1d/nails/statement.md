---
id: a8b0dd50-d38c-47f3-85d4-d95ff71f364b
longname: Гвоздики
languages: [python, cpp]
tags: [dynamic]
checker: cmp_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


В дощечке в один ряд вбиты гвоздики. Любые два гвоздика можно соединить ниточкой. Требуется соединить некоторые пары гвоздиков ниточками так, чтобы к каждому гвоздику была привязана хотя бы одна ниточка, а суммарная длина всех ниточек была минимальна.

### Формат входных данных

В строке заданы N (2 <= N <= 100) чисел — координаты всех гвоздиков (неотрицательные целые числа, не превосходящие 10000).

### Формат выходных данных

Выведите единственное число — минимальную суммарную длину всех ниточек.

### Примеры

```
-> 4 10 0 12 2
--
<- 6
```

```
-> 3 4 12 6 14 13
--
<- 5
```
