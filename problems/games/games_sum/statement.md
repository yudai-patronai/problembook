---
id: 261526ec-8343-4b67-aee4-bbbbbdeba5e4
longname: Сумма игр
languages: [python]
tags: [games]
checker: cmp_yesno
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Дано N кучек камней разного размера. За один ход можно выбрать одну непустую кучку и выкинуть из нее
не более, чем K камней. Игроков двое, ходят по очереди. Выиграет тот, кто опустошит последнюю кучку камней.

### Формат входных данных

На первой строке дано два положительных числа N ≤ 1000 и K ≤ 500. На второй строке даны N
положительных чисел - размеры кучек камней. Размеры не превышают 500.

### Формат выходных данных

Выведите YES, если у первого игрока есть выйгрышная стратегия. Иначе, выведите NO.

### Примеры

```
-> 4 2
-> 5 3 6
--
<- YES
```

```
-> 1 6
-> 14
--
<- NO
```