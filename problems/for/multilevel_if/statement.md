---
fixme: true
id: 51a10767-0d01-415c-b469-8162503dec52
longname: Суеверный Петя
tags: [for, if]
languages: [cpp]
checker: cmp_int_seq
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

На вход подается последовательность четырехзначных натуральных чисел из N элементов. Петя не любит, когда число делится на 4, 7 и 9. Однако для каждого "деления" его ненависть пропадает, если выполняются соответсвенно следующие условия: если число делится на 4, но начинается на 4 или 5; если число делится на 7, но начинается на 7 или 1; если число делится на 9, но начинается на 9 или 8. Необходимо в введенной последовательности выявить неприятные Пете числа и вывести их на экран.
Если их нет - вывести 0.

### Формат входных данных

Натуральное число N.
На следующей строчке N четырехзначных натуральных чисел.

### Формат выходных данных

Последовательность неприятных чисел. Либо 0, если таких чисел нет.

### Примеры

```
-> 5
-> 1004 6005 9999 1001 3994
--
<- 1004 
```

```
-> 3
-> 5005 3395 1234
--
<- 5005
<- 3395
```

```
-> 2
-> 2042 6666 
--
<- 0
```