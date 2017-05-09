---
id: 7879c456-6b2d-492f-929e-75895ad05ce8
longname: А-функция
tags: [strings]
checker: cmp_int_seq
time_limit: 4
real_time_limit: 4
max_vm_size: 256M
---

Зафиксируем строку L. Будем называть её подстроку K особенной, если у неё есть как минимум три различных вхождения в L, среди которых префикс и суффикс строки L.

Пусть теперь дана строка S, состоящая из N символов. Пусть B(i) - длина максимальной особенной подстроки у строки, образованной первыми i символами S.


Напишите программу, которая вычислит значения функции B для заданной строчки для всех возможных значений i от 1 до N (нумерация от 1).

Входные данные
В единственной строке записана строка, состоящая только из больших и/или маленьких латинских букв. Длина строки 1 <= N <= 200000.

Выходные данные
В выходной файл выведите N чисел — значения функции B(1), B(2), … B(N).
### Примеры

```
-> aaaaa
--
<- 0 0 1 2 3
```

```
-> abacabacabacaba
--
<-
```
