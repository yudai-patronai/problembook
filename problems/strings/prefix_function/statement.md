---
id: f8158168-7725-4489-ae3a-0c278e0cf875
longname: Префикс функция
tags: [strings]
checker: cmp_int_seq
time_limit: 1
real_time_limit: 1
max_vm_size: 256M
---

Посчитать префикс функцию для строки.

Примечание: для вывода массива чисел рекомендуется использовать print(" ".join(map(str, numbers))). Многократный вызов print в цикле может привести к TL.

### Формат входных данных

В первой строке заданная строка из маленьких букв латинского алфавита. Длина строки не превышает 100000.

### Формат выходных данных

Массив чисел через пробел, представляющих значения префикс функции

### Примеры

```
-> aaaa
--
<- 0 1 2 3
```

```
-> ababcabd
--
<- 0 0 1 2 0 1 2 0
```