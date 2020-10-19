---
id: 060e2375-f1a0-4c3b-8412-9a2b50606b2d
longname: Уравнение ax=b (mod m)
languages: [python]
tags: [cycles,modulo]
checker: cmp_int_seq
time_limit: 1
real_time_limit: 1
max_vm_size: 16M
---

Решить сравнение `a*x ≡ b (mod m)`.

Решением здесь называется целое неотрицательное число, меньшее m, удовлетворяющее сравнению.

### Формат входных данных

Три строки: m (натуральное), a (целое), b (целое).

### Формат выходных данных

Через пробел все решения сравнения в порядке возрастания (**нельзя использовать сортировку**).

Если решений нет, вывести -1.

### Примеры

```
-> 3
-> 2
-> 1
--
<- 2
```

```
-> 26
-> 8
-> 7
--
<- -1
```