---
id: 5e36b7fd-7839-4f63-bbd4-86209619bcba
longname: Поиск подстроки в строке
tags: [strings]
checker: cmp_int_seq
time_limit: 2
real_time_limit: 2
max_vm_size: 256M
---

Найти все вхождения строки A в строке B.

Примечание: для вывода массива чисел рекомендуется использовать print(" ".join(map(str, numbers))). Многократный вызов print в цикле может привести к TL.

### Формат входных данных

В первой строке вводится строка A, во второй строка B.
Обе строки состоят из маленьких латинских букв. Суммарная длина строк не превышает 200000.

### Формат выходных данных

Все вхождения через пробел. Нумерация позиций с 0.
Если вхождений нет нужно вывести -1.

### Примеры

```
-> aaa
-> aaaaa
--
<- 0 1 2
```

```
-> abc
-> abdcab
--
<- -1
```