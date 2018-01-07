---
fixme: true
id: a5d2199e-366b-4fee-9135-ef33b1f6f479
longname: Подсчет количества слов в файле
tags: [string]
languages: [cpp]
checker: cmp_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Посчитать количество слов в файле.

### Формат входных данных

На вход подается не пустой файл input.txt, содержащий текст произвольной длинны. Слова разделяются пробелами и содержат только буквы английского алфавита.

### Формат выходных данных

Неотрицательное целое число C — количество слов в файле.

### Примеры

```
-> input.txt [Hello, world]
--
<- 2
```

```
-> intput.txt [Mary had a little lamb]
--
<- 5
```