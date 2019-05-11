---
id: 8a13b8f6-b127-44ca-a723-ebadc1f40139
longname: Степень строки
languages: [python]
tags: [string]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Пусть задана строка s. Назовем ее k-ой (k > 0) степенью s^k строку s^k = sss (k раз). Например, третьей степенью строки abc является строка аbсаbсаbс.

Корнем k степени из строки s называется такая строка t (если она существует), что t^k = s.

Ваша задача состоит в том, чтобы написать программу, находящую степень строки или корень из нее.

### Формат входных данных

На вход программе подается 2 строки. Первая содержит строку S, вторая - степень k.
Отрицательная степень означает взятие корня соответствующей степени.

### Формат выходных данных

Вывести строку, являющуюуся ответом на задачу. Если такой строки нет, то нужно вывести 'NO SOLUTION' (без кавычек).

### Примеры

```
-> abc
-> 3
--
<- abcabcabc
```

```
-> abcdabcd
-> -2
--
<- abcd
```

```
-> abcd
-> -4
--
<- NO SOLUTION
```