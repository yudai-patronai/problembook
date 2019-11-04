---
id: 358147ae-3db1-41d2-bbae-78943ed44bcd
longname: Быстрые сортировки - сортировка Тони Хоара
languages: [python]
tags: [sort,standart]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Сортировка Тони Хоара заключается в следующем:
- разбиение массива по барьеру
- сортировка элементов, меньших барьера (группа 1) - рекуррентный вызов
- сортировка элементов, больших барьера (группа 3) - рекуррентный вызов
- пересборка исходного массива "склеиванием" элементов группы 1, затем элементов, равных барьеру (группа 2) и элементов группы 3

В этой задаче вам необходимо реализовать сортировку Тони Хоара, в которой в качестве барьера используется элемент массива на позиции 0.

Для написания функции воспользуетсь шаблоном, приведённом ниже.
Ваш код должен находиться между вызовами функции `print`.
Отправлять на проверку нужно всю функцию `hoar_sort`.

### Шаблон функции

```
def hoar_sort(A, depth=1, part='left'):
    print('depth:', depth, 'part:', part, 'array before:', A)

    #  ваша реализация сортировки

    print('depth:', depth, 'part:', part, 'array after:', A)
```

### Аргументы функции

1. `A` - список из целых чисел, над которым осуществляется сортировка.
2. `depth` - глубина рекурсивного вызова, отсчёт начинает с единицы, не забудьте передать глубину в последующие вызовы.
3. `part` - строка, имеющая одно из двух значений: `left` или `right`, при рекурсивном вызове сортировки от левой части подавать значение `left`, при сортировке правой части - `right`. Первый вызов считается `left`.

### Возвращаемое значение функции

Функция не возвращает значений.
Она производит только печать, как указано в шаблоне и сортирует по возрастанию массив `A` (inplace).

### Примеры

```
-> >>> solution.hoar_sort([5, 2, 4, 8, 7, 1, 3, 10, 6])
--
<- depth: 1 part: left array before: [5, 2, 4, 8, 7, 1, 3, 10, 6]
<- depth: 2 part: left array before: [2, 4, 1, 3]
<- depth: 3 part: left array before: [1]
<- depth: 3 part: right array before: [4, 3]
<- depth: 4 part: left array before: [3]
<- depth: 4 part: right array before: []
<- depth: 3 part: right array after: [3, 4]
<- depth: 2 part: left array after: [1, 2, 3, 4]
<- depth: 2 part: right array before: [8, 7, 10, 6]
<- depth: 3 part: left array before: [7, 6]
<- depth: 4 part: left array before: [6]
<- depth: 4 part: right array before: []
<- depth: 3 part: left array after: [6, 7]
<- depth: 3 part: right array before: [10]
<- depth: 2 part: right array after: [6, 7, 8, 10]
<- depth: 1 part: left array after: [1, 2, 3, 4, 5, 6, 7, 8, 10]
```
