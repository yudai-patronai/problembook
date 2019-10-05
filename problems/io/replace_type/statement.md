---
id: 3a1c93c9-ec58-4d68-a112-0380d1ae4f72
longname: Преобразование типов
languages: [C]
tags: [pointer]
checker: cmp_file
time_limit: 10
real_time_limit: 10
max_vm_size: 64M
---


На вход вашей программе подается целое число типа `unsigned long int` и целевой тип. Вам необходимо написать программу, которая выводи на экран число (или символ), представленный той же последовательностью бит, что и исходное число. Если размер переменной целевого типа меньше исходного, необходимо напечатать последовательность чисел.

Целевые типы:

* "sint" -- `short int`
* "lint" -- `long int`
* "usint -- `unsigned short int`
* "ulint" -- `unsigned long int`
* "uchar" -- `unsigned char` (как число)
* "dchar" -- `char` (как число)
* "schar" -- `char` (как символ)
* "float" -- `float`

### Формат входных данных

На первой строке передается входное число типа `unsigned long int`, на второй строке целевой тип в соответствии с таблицей.

### Формат выходных данных

Число или посследовательность чисел (символов) -- результат работы программы.

### Примеры

```
-> 42
-> ulint
--
<- 42
```

```
-> 18222222222222222222
-> lint
--
<- -224521851487329394
```