---
id: 5d0bdf52-4aa5-4b71-8af5-5bea9daab617
longname: Разложение десятичного числа по степеням
languages: [python]
tags: [numeral_system,strings,while]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Разложите неотрицательное целое десятичное число по степеням основания.

Слагаемое разложение должно быть записано слитно в формате: `цифра*10^разряд`. Слагаемые разделяются тремя символами: ` + ` (пробел, знак плюс, пробел). Слагаемые должны располагаться по убыванию разряда.

### Формат входных данных

Нетрицательное целое десятичное число.

### Формат выходных данных

Одна строка.

### Примеры

```
-> 193
--
<- 1*10^2 + 9*10^1 + 3*10^0
```
