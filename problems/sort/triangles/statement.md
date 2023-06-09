---
id: 97bed6d9-2775-4ba8-b80b-b2fdeac5a2ef
longname: Сортировка треугольников
languages: [python]
tags: [sort]
source_header: header.py
source_footer: footer.py
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Требуется отсортировать треугольники по возрастанию их площадей. Если площади равны, то отсортировать по идентификаторам лексикографически.


### Формат входных данных

На первой строке N, количество треугольников. На каждой следующей из N строк: идентификатор треугольника (строка из непробельных символов), и длина 3 сторон треугольника через пробел. Треугольники обязательно существуют. Обязательно написать и использовать свой класс Triangle!

### Формат выходных данных

Те же N строк, но отсортированных по возрастанию площадей треугольников.

### Примеры

```
-> 3
-> id1 2 3 4
-> id2 7 8 9
-> id3 4 5 6
--
<- id1 2 3 4
<- id3 4 5 6
<- id2 7 8 9
```

```
-> 2
-> triangle0 2 4 3
-> triangle1 1 1 1
--
<- triangle1 1 1 1
<- triangle0 2 4 3
```

```
-> 2
-> triangle3 1 1 1
-> triangle2 1 1 1
--
<- triangle2 1 1 1
<- triangle3 1 1 1
```
