---
fixme: true
id: 213e015f-324e-42ce-b29d-990bcdd73859
longname: Проверка выполнения свойств кучи в массиве
languages: [python]
tags: [sort]
checker: cmp_yesno
time_limit: 1
real_time_limit: 5
max_vm_size: 64M
---


Двоичная куча - двоичное дерево, в котором выполняются три условия:
1. Значение в любой вершине не меньше, чем значения ее потомков.
2. Глубина всех листьев отличается не более, чем на 1.
3. Последний слой заполняется слева направо.

О свойствах `2` и `3` мы уже побеспокоились за Вас. Элемент под номером `0` является корнем дерева. Для элемента под номером `i` потомки будут иметь номера `2*i+1` и `2*i+2`. Например, для элемента `0` потомки будут иметь номера `1` и `2`. Ваша задача проверить данный вам массив на выполнение свойства `1`. 

### Формат входных данных

Дано натуральное число N <= 10<sup>6</sup>. Далее идут N элементов |a<sub>i</sub>| <= 10<sup>6</sup>. 

### Формат выходных данных

Необходимо вывести одно слово без кавычек: "YES", если свойство выполняется, иначе "NO".

### Примеры

```
-> 5
-> 8
-> 6
-> 1
-> 5
-> 2
--
<- YES
```

```
-> 3
-> 6
-> 7
-> 3
--
<- NO
```