---
id: 7879c456-6b2d-492f-929e-75895ad05ce8
longname: А-функция
tags: [strings]
checker: cmp_int_seq
time_limit: 4
real_time_limit: 4
max_vm_size: 256M
---

Дана строка S, состоящая из N символов. Определим функцию A(i) от первых i символов этой сроки следующим образом:

A(i) = максимально возможному k, что равны следующие строки:

S[1]+S[2]+S[3]+…+S[k]

S[i]+S[i–1]+S[i–2]+…+S[i–k+1]

где S[i] – i-ый символ строки S (нумерация символов с 1), а знак + означает, что символы записываются в строчку непосредственно друг за другом.

Напишите программу, которая вычислит значения функции A для заданной строчки для всех возможных значений i от 1 до N.

Входные данные
В единственной строке записана строка, состоящая только из больших и/или маленьких латинских букв. Длина строки 1 <= N <= 200000.

Выходные данные
В выходной файл выведите N чисел — значения функции A(1), A(2), … A(N).
### Примеры

```
-> aabaa
--
<- 1 2 0 1 5
```