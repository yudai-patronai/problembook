---
fixme: true
id: b34e19a4-71fd-4081-8224-4502922803d8
longname: Разбиение массива на три группы
languages: [python]
tags: [sort]
time_limit: 1
real_time_limit: 5
max_vm_size: 64M
---


Вам необходимо написать **функцию** `split_array(arr, n, x)`, которая **изменяет** массив `arr` длины `n` таким образом, что сначала в массиве будут идти числа строго меньше, чем `x`, далее числа равные ему, и в конце числа больше, чем `x`. Порядок чисел внутри каждой группы не имеет значения.

### Формат входных данных

На вход функции передаются: массив чисел, его длина и один из элементов массива. Гарантируется, что элементы массива по модулю не превосходят 10<sup>6</sup>. Сам массив не пустой и содержит не более 10<sup>6</sup> элементов.

### Формат выходных данных

Ваша функция должна изменить переданный ей массив так, чтобы сначала шли числа меньше `x`, затем равные ему, потом больше. Возвращать результатом функции ничего не надо.

### Примеры

``` 
-> [4, 8, 6, 1, 3, 5, 7]
-> 7
-> 3
--
<- [1, 3, 4, 8, 6, 5, 7]
```

```
-> [5, 7, 6, 5, 11, 8, 5]
-> 7
-> 5
--
<- [5, 5, 5. 6, 7, 11, 8]
```