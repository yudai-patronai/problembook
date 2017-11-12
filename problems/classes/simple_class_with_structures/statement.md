---
id: d5383850-b53c-43cc-8642-69efbe4637b8
longname: Класс с массивом структур
languages: [cpp]
tags: [classes]
source_footer: footer.cpp
checker: cmp_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Написать класс MyClass с одним полем - массив структур. В классе должны быть реализованы два метода:
AddElement() - добавить новую структуру в массив. В случае уже наличия таковой - ничего не делать.
PrintStructures() - распечатать содержимое элементов массива в формате int string.
Структура содержит в себе поле int и string строку.

### Формат выходных данных

Число и строка, разделённые пробелом

### Пример

```
-> 1 hello
-> 2 hi
-> 2 hi
--
<- 1 hello
<- 2 hi
```
