---
id: ab46d419-f4bf-461b-8403-421a45fa6605
longname: Нахождение вершины-"столицы"
tags: [graphs,floyd]
checker: cmp_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

В некотором государстве некотрые города соединены дорогами. Жители этого некоторого государства просят вас помочь им с выбором столицы: требуется, чтобы сумма расстояний от столицы до каждого из остальных городов была минимальна.

Для вашего удобства города уже пронумерованы от `0` до `n-1`.

На вход программе в первой строке подается два числа через пробел: `n` и `m`. `n` (2 <= `n` <= 100) - число городов, `m` (1 <= `m` <= 500) - число дорог.
В следующих `m` строках задаются дороги, по три числа в каждой строке - номера соединенных городов и длина дороги.

Выведите номер столицы. Если возможно несколько варинтов выведете любой.

-> 4 3
-> 0 1 34
-> 2 1 7
-> 3 2 85
--
<- 1


-> 8 9
-> 6 3 91
-> 0 4 92
-> 6 7 56
-> 1 6 99
-> 1 5 66
-> 0 2 64
-> 3 5 75
-> 0 1 33
-> 0 3 19
--
<- 0