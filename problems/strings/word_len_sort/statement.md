---
id: 462ef47d-bdc8-4a09-a4ef-8d8008832c5e
longname: Сортировка слов по длине
languages: [python]
tags: [strings]
checker: cmp_int_seq
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Вводится строка, состоящая из слов, разделенных пробелами. Требуется отсортировать слова в строке так, чтобы наиболее короткие из них были вначале строки, а наиболее длинные в конце. Вывести сумму кодов букв, из которых состоят отсортированные слова. Если слова имеют одинаковую длину, они должны быть отсортированы в алфавитном порядке.

Для сортировки можно использовать встроенную в Python функцию sorted(). Напоминаем, что узнать о параметрах встроенных в Python функций можно, воспользовавшись функцией help() в интерпретаторе python3.

### Формат входных данных

Строка со словами, разделенными пробелами.

### Формат выходных данных

Последовательность суммы кодов

### Примеры

```
-> abcd hi efg
--
<- 209 306 394
```

```
-> bb bbb aaa
--
<- 196 291 294
```
