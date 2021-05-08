---
id: c3af8771-b04a-43c6-a010-405022217d4b
longname: Время дороги в метро
languages: [python]
tags: [dfs]
checker: cmp_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


В этой задаче необходимо подсчитать время в пути (минут) от одной станции московского метро `start` до другой `end`.

### Формат входных данных

В первой строке 4 значения через пробел `V E start end`.

- `V` - число станций
- `E` - число соединений между станциями
- `start` - название отправной станции
- `end` - название конечной станции

Далее следуют `E` строк в формате `name_1 name_2 time`:

- `name_1` и `name_2` - связанные между собой станции метро (железной дорогой или переходом)
- `time` - время в минутах, которое требуется, чтобы попасть из станции `name_1` на станцию `name_2`  

### Формат выходных данных

Одно число — результат.

### Примеры

```
-> 6 5 mendeleevskaya serpukhovskaya
-> mendeleevskaya tsvetnoy_bulvar 4
-> tsvetnoy_bulvar chekhovskaya 3
-> chekhovskaya borovitskaya 4
-> borovitskaya polyanka 3
-> polyanka serpukhovskaya 3
--
<- 17
```
