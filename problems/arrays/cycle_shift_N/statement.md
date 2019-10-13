---
id: b1a4dbc2-1dab-498b-b38c-0940a9259a55
longname: Длинное название задачи
languages: [python]
tags: [arrays, functions]
checker: cmp_yesno
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Циклическим сдвигом массива влево на `M` позиций называется операция, при которой индексы всех элементов,
смещаются на M позиций влево, при этом если, некоторый элемент имеет индекс меньше `i < М`, то он должен быть
помещен в позицию `N - M + i`, где индекс элемента `i` отсчитывается от `0`. Сдвиг также должен корретно работать
для значений `M > N`.

В данной задаче Вам необходимо написать **функцию**

+ python: `cycle_shift(arr, N, M)`,

где `arr` -- исходный массив, `N` -- длина этого массива, `M` -- величина сдвигаю

В результате работы функции над массивом `arr` должна быть выполнена операция циклического сдвига влево. Сдвиг следует проводить in place, без использования дополнительного массива.

**Внимание! В данной задаче необходимо реализовать только функцию! Ввод и вывод данных писать не нужно!**

### Формат входных данных

Функция должна принимать на вход 3 аргумента: массив `arr`, число `N` -- длина массива `arr`,
`M` -- величина сдвига. `0 < N < 100`.

### Формат выходных данных

Функция не должна возвращать никаких значений.
Результатом работы является измененный исходный массив `arr`.
### Примеры

```
-> arr = [1, 2, 3, 4, 5]
-> N = 5
-> M = 2
--
<- [3, 4, 5, 1, 2]
```

```
-> arr = [1]
-> N = 1
-> M = 5
--
<- [1]
```

```
-> arr = [1, 2, 3]
-> N = 3
-> M = 8
--
<- [3, 1, 2]
```
