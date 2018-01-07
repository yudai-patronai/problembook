---
fixme: true
id: f6a72564-4f38-465d-b34e-c0fe56336b25
longname: Количество элементов, превосходящих опорный
languages: [python]
tags: [arrays,sort]
checker: cmp_int
time_limit: 1
real_time_limit: 5
max_vm_size: 64M
---

На вход программе подается массив из N чисел и индекс опорного элемента. Необходимо найти количество элементов в массиве больше опорного.

### Формат входных данных

В первой строчке программе подается число N -- количество элементов массива. Далее на N строках идут элементы этого массива.

Далее в новой строке вводится число M<N -- индекс опорного элемента.

### Формат выходных данных

Необходимо вывести одно число -- количество элементов больше опорного.

### Примеры

```
-> 5
-> 1
-> 2
-> 3
-> 4
-> 5
-> 3
--
<- 2
```

```
-> 5
-> 1
-> 2
-> 3
-> 4
-> 5
-> 1
--
<- 4
```