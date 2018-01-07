---
id: c57be5c2-ead4-41a3-a0f0-b346dabc952d
longname: Наибольший прямоугольник
languages: [python]
tags: [arrays,functions]
checker: cmp_int
time_limit: 1
real_time_limit: 2
max_vm_size: 64M
---

Вам дается массив целых неотрицательных чисел -- количество и высота столбцов гистограммы. Вам необходимо определить максимальную площадь прямоугольника, который можно вписать в данную гистограмму. 
Шириной прямоугольника является количество столобцов, которые захватывает прямоугольник, высотой будет наименьшая высота столбца среди всех, находящихся в этом диапазоне.

Вам необходимо реализовать **функцию** `largest_rect(N, array)`. Функция принимает на вход длину массива и сам массив столбцов гистограммы. Функция должна вернуть одно число -- площадь наибольшего прямоугольника

### Формат входных данных

На вход функции передается одно число -- размер массива и массив чисел -- высоты столбцов гистограммы. Значения высоты столбца не превосходит 1000, длина массива не превосходит 100.

### Формат выходных данных

Функция должна возвращать одно число -- площадь наибольшего прямоугольника.

### Примеры

>> largest_rect(5, [1,3,5,3,1])
>> 9

>> largest_rect(5, [3,3,3,3,3])
>> 15

