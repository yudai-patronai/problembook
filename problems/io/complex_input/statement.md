---
id: dae94af0-3eb9-4c5f-b7f5-e6f78e6c38e2
longname: Статистика занятий
languages: [python]
tags: [io,simple]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Вам предоставляется информация о фамилии студента, потраченных им часов учебные предметы, а также оценки по этим предметам.

Статистика (часы занятий и оценки) записываются в следующем формате:

`<часы М> <оценка М> <часы Ф> <оценка Ф> <часы И> <оценка И>`

где `М`, `Ф`, и `И` это обозначения для предметов: математика, физика и информатика соответственно.

Количество часов может быть дробным, оценка - натуральное число от 1 до 10.

Необходимо найти

- общее количество часов, потраченное на три предмета
- среднюю оценку по трём предметам

Ответ округляйте с точностью до одного знака после запятой.

### Формат входных данных

Две строки. Первая содержит фамилию студента. Вторая содержит 6 чисел через пробел в формате, описанном выше.

### Формат выходных данных

Одна строка, содержащая три значения через пробел: фамилия студента, общее количество часов, средняя оценка.

### Примеры

```
-> Pupkin
-> 75.5 8 105.5 9 45.1 8
--
<- Pupkin 226.1 8.3
```
