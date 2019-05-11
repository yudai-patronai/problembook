---
id: 1716a40e-b886-4014-86e9-df8583df8b29
longname: Банковский вклад
languages: [python]
tags: [while]
checker: cmp_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Вклад в банке составляет x рублей. 
Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается. 
Каждый год сумма вклада становится больше. 
Надо определить, через сколько лет вклад составит не менее y рублей.

### Формат входных данных

Три натуральных числа: x, p, y.

### Формат выходных данных

Число лет, через сколько лет вклад составит не менее y рублей.

### Примеры

```
-> 100 10 200
--
<- 8
```

```
-> 1 1 2
--
<- 100
```