---
id: dc1174b8-1eda-4ffd-8be8-06f6b6db6b51
longname: Полеты Аэрофлота
languages: [cpp,]
tags: [classes]
checker: cmp_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Вам дается список рейсов аэрофлота в формате: пункт_вылета пункт_назначения день_вылета_1 день_вылета_2 день_вылета_3.
Под временем понимается день месяца. Дни нумеруются от 0 до 30.
Требуется найти, сколько полетов совершается из пункта А в пункт B после дня m (время_вылета_x >= m).

### Формат входных данных

Cначала идет число рейсов n.
Затем n строк содержащие по 5 чисел - описание рейсов.
Рейсы описываются в формате: id_вылета id_прилета день_вылета_1 день_вылета_2 день_вылета_3
Затем идет 3 числа: интересующий аэрорт вылета, интересующий аэропорт прилета, день m.

### Формат выходных данных

Одно число — результат.

### Примеры

```
-> 2
-> 1 2 5 8 10
-> 2 5 10 20 30
-> 1 2 7
--
<- 3
```
