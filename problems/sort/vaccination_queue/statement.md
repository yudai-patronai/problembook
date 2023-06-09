
---
id: 6eb3d9f6-01f5-4cfe-959a-1360dcab08b7
longname: Очередь на вакцинирование
languages: [cpp]
tags: [sort]
checker: cmp_unsigned_int_seq
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


После изобретения вакцины от KOROVA-вируса все жители города Мозгва торопятся пройти вакцинацию, поэтому в медицинское учереждение образовалась электронная очередь.

Поскольку самыми уязвимыми для данной инфекции являются возрастные пациенты, их решено прививать в первую очередь.

Зная ваши навыки по сортировке массивов, правительство Мозгвы призвало вас написать алгоритм, который поставит самых пожилых людей в начало очереди, а самых молодых — в конец. Чтобы не возникло конфликтов, важно не перепутать исходный порядок людей с одинаковым возрастом.

В связи с законом о защите персональных данных информация о гражданах деперсонализирована — каждому человеку присвоен уникальный ID.

### Формат входных данных

В первой строке вам дано число жителей N, при этом N > 3, N <= 10000.
В последующих N строках записаны через пробел по два числа — ID жителя и его возраст.

### Формат выходных данных

На выходе вам нужно вывести N строк с идентификаторами, отсортированными по убыванию возраста жителей. Возраст указывать не нужно.

### Примеры

```
-> 3
-> 1 50
-> 2 60
-> 3 50
--
<- 2
<- 1
<- 3
```

