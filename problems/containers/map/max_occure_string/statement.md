---
id: 290f937d-4055-452f-8257-f62479fe679f
longname: Самoе популярое слово
languages: [cpp,python]
tags: [map,containers,easy]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Найти самое популярное слово из данных без учёта регистра и найти количество его вхождений.

### Формат входных данных

На первой строке `n` (0 < `n` <= 1000) — количество слов.
Далее `n` строк, которые являются данными словами (вся строка является словом, пробелов нет).

### Формат выходных данных

Через пробел искомое слово в нижнем регистре и количество его вхождений.

### Примеры

```
-> 3
-> Aa
-> aa
-> Aaa
--
<- aa 2
```

```
-> 4
-> AaA
-> aAa
-> AAA
-> AAa
--
<- aaa 4
```
