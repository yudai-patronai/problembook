---
fixme: true
id: 59baa314-79f8-4b22-97bd-35ac1fe61e60
longname: Функция Аккермана
languages: [python]
tags: [recursion]
checker: cmp_int
time_limit: 5
real_time_limit: 5
max_vm_size: 64M
---


Вычислить функцию Аккермана, которая задается следующим образом:

A(m,n) = n+1 при m = 0,
A(m,n) = A(m-1,1) при m > 0, n = 0
A(m,n) = A(m-1,A(m,n-1)) при m,n > 0

### Формат входных данных

Два числа m и n.

### Формат выходных данных

A(m, n)

### Примеры

```
-> 1
-> 1
--
<- 3
```

```
-> 4
-> 0
--
<- 13
```
