---
id: c380477d-cac4-4a45-9ff5-7b0f7d60c0f6
longname: Лифт
languages: [python]
tags: [binsearch]
checker: cmp_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
fixme: true
---


В здании из **N** этажей есть один лифт. В данный момент он находится на парковке (один этаж ниже первого). Лифт может перевозить не более **C** человек одновременно. На преодоление расстояния в 1 этаж у лифта уходит **P** секунд. На i этаже находится **A<sub>i</sub>** человек для всех i от 1 до N включительно. Каково наибольшее количество человек, которых лифт способен перевезти на парковку за **T** секунд?

### Формат входных данных

В первой строке находятся четыре натуральных числа N, C, P, T.

Вторая строка содержит N целых неотрицательных чисел A<sub>i</sub>.

### Формат выходных данных

Одно число — наибольшее количество человек, которых лифт успеет перевезти на парковку.

### Примеры

```
-> 4 5 2 15
-> 0 1 2 3
--
<- 3
```

```
-> 4 5 2 18
-> 0 1 2 3
--
<- 5
```

```
-> 3 2 1 9
-> 1 1 1
--
<- 3
```