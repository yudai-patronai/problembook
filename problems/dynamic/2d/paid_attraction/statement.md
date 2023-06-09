---
id: aedeec91-922a-4a12-8df6-a94dd4cd5432
longname: Платный аттракцион
languages: [python]
tags: [dynamic, 2d]
checker: cmp_file
time_limit: 1
real_time_limit: 5
max_vm_size: 64M
---


В парке развлечений Васе попался аттракцион.

Это прямоугольное поле NxM.
Вася начинает свой путь в левой верхней клетке, а заканчивает в правой нижней.
По правилам аттракциона Вася может двигаться только вниз и вправо и должен платить штраф p<sub>ij</sub> за прохождение клетки.
Вася взял с собой не так уж и много денег, поэтому он хочет пройти аттракцион, потратив как можно меньше.

Помогите Васе узнать, сколько денег у него останется.

### Формат входных данных

На первых двух строках даны два натуральных числа M и N, не превосходящие 100.

Далее идут NM чисел, задающих штрафы p<sub>ij</sub> на поле.
Первые N чисел задают штрафы в первой строке поля, вторые N чисел - во второй и так далее...
Гарантируется, что штрафы неотрицательны и не превосходят 1000: 0 ≤ p<sub>ij</sub> ≤ 1000.

На последней строке лежит целое число C ≤ 1000000, сумма денег у Васи.

### Формат выходных данных

Если Васе хватает денег, то выведите одно число — оставшуюся сумму денег у Васи.
Если Васе не хватает денег, чтобы добраться до целевой клетки, выведите строку `Impossible`.

### Примеры

```
-> 3
-> 3
-> 0
-> 2
-> 1
-> 4
-> 2
-> 3
-> 1
-> 2
-> 1
-> 8
--
<- 1
```

```
-> 3
-> 3
-> 0
-> 2
-> 1
-> 4
-> 2
-> 3
-> 1
-> 2
-> 1
-> 5
--
<- Impossible
```
