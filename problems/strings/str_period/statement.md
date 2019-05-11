---
id: 3efbe0c4-e141-4fbb-81f0-bcc806e6006f
longname: Период строки
languages: [python]
tags: [string]
checker: cmp_int
time_limit: 2
real_time_limit: 5
max_vm_size: 64M
---

Дана непустая строка s.
Нужно найти такое наибольшее число k, что s совпадает со строкой t, выписанной k раз подряд.

### Формат входных данных

Одна строка длины N, 0 < N ≤ 10^6, состоящая только из маленьких латинских букв.

### Формат выходных данных

Одно число - наибольшее возможное k.

### Примеры

```
-> aaaaa
--
<- 5
```

```
-> abcabcabc
--
<- 3
```

```
-> abab
--
<- 2
```