---
id: cd0bfd22-cfc4-4cd0-a28c-783717d148e6
longname: Анатомия матрёшки
languages: [python]
tags: [recursion,easy,print]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


В этой задаче необходимо создать функцию `matryoshka(n)`, которая по заданному натуральному числу `n` печатает матрёшку.

Каждая матрёшка обладает уровнем вложенности.
Все матрёшки, кроме самой маленькой, состоят из верха и низа.
Печать должна отражать, как верхи и низы матрёшек согласуются между собой и самой маленькой (цельной) матрёшкой.

Верх матрёшки уровня `i` нужно показать, напечатав `verh matryoshki i`.
Низ матрёшки уровня `i` нужно показать, напечатав `niz matryoshki i`.
Положение самой маленькой матрёшки показывается печатью `matryoshechka`.

В этой задаче необходимо обойтись без циклов `for` и `while`.

### Описание аргументов функции

Функция `matryoshka(n)` имеет один аргумент `n` - целое число, уровень вложенности (размер) матрёшки.

### Формат возвращаемого функцией значения

Функция `matryoshka(n)` производит только печать, значений не возвращает.

### Примеры вызова функции

    >>> matryoshka(3)
    verh matryoshki 3
    verh matryoshki 2
    matryoshechka
    niz matryoshki 2
    niz matryoshki 3
