---
id: 846ddf10-4d95-439a-a2e9-b91a20622f23
longname: "Сортировка: сначала чётные"
tags: [sort,easy]
checker: cmp_intseq
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Дан список целых чисел. Отсортировать его так, чтобы сначала шли чётные по возрастанию, потом — нечётные во возрастанию.

### Формат входных данных

Одна строка — список чисел через пробел. Длина списка не превосходит 10000.

### Формат выходных данных

Отсортированный список чисел через пробел.

### Примеры

```
-> 1 2 3 4 5
--
<- 2 4 1 3 5
```

```
-> 8 7 6 5 4 2 12
--
<- 2 4 6 8 12 5 7
```