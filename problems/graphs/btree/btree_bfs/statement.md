---
id: 9c37c4a9-5ec5-4c96-8567-19a8984ee87e
longname: Дерево - обход в ширину
tags: [graphs,binary,tree,btree]
languages: [python, cpp]
checker: cmp_long_long_seq
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Реализуйте обход в ширину бинарного дерева поиска для целых чисел. Программа получает на вход последовательность различных натуральных чисел и строит из них дерево. Элементы в деревья добавляются в соответствии с результатом поиска их места. Балансировка дерева не производится. Распечатайте полученное дерево по этажам, начиная от корня. Для этого:

    заведите очередь из узлов деревьев
    положите корень дерева в очередь
    пока очередь не пуста:
        возьмите узел из очереди
        распечатайте его
        положите левого ребенка в очередь, если он есть
        положите правого ребенка в очередь, если он есть

### Формат входных данных

На вход программа получает последовательность натуральных чисел меньших 10000.

### Формат выходных данных

Узлы бинарного дерева по этажам через пробел.

### Примеры

```
-> 5 15 18
--
<- 5 15 18
```

```
-> 12 26 23 28 33 8
--
<- 12 8 26 23 28 33
```

```
-> 35 8 6 48 30 17 4 43 42
--
<- 35 8 48 6 30 43 4 17 42
```
