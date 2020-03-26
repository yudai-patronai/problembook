---
fixme: true
id: f8cebdfd-15ea-4db1-88da-7464c0a52f38
longname: Сортировка кучей
languages: [python]
tags: [sort,heap]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Напишите функцию `heapsort(A)`, выполняющую сортировку кучей массива целых чисел `A` **по возрастранию**.
Сортировка должна происходить в самом массиве `A`, без выделения дополнительных массивов.

Во время разработки пользуйтесь кучей с максимальным элементом в корне (max-heap).

Также, функция `heapsort(A)` должна производить следующую печать:
1. одноразовая печать массива `A` сразу после превращения его в кучу,
2. печать массива `A` в конце каждой итерации цикла сортировки.

Массив печатайте на одной строке с пробелом между элементами.

Ваш код может включать и другие функции.

### Аргументы функции

- `A` - массив (`list`) целых чисел

### Возвращаемое значение

Функция `heapsort` не возвращает значений, но печатает состояния `A` (см. условие выше).

### Примеры работы функции

    >>> heapsort([3,2,5,0,-1])
    5 2 3 0 -1  # начальное состояние - куча (max-heap)
    3 2 -1 0 5  # далее печать после каждой итерации (всего прошло 4 итерации)
    2 0 -1 3 5 
    0 -1 2 3 5
    -1 0 2 3 5 