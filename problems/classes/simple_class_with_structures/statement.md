---
id: d5383850-b53c-43cc-8642-69efbe4637b8
longname: Класс с массивом структур
languages: [cpp]
tags: [classes]
source_header: header.cpp
source_footer: footer.cpp
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Написать класс MyClass с одним полем - `std::vector` структур. В классе должны быть реализованы два метода:
addElement() - добавить новую структуру в массив. В случае уже наличия таковой - ничего не делать.
printStructures() - распечатать содержимое элементов массива в формате "число строка" (через пробел).
Структура содержит в себе поле int и std::string строку.

### Формат выходных данных

Вывод в стандартный поток вывода происходит в результате вызова obj.PrintStructures().
В резултате выводятся все хранимые структуры, каждая в новой строке, при этом число и строка разделены пробелом.

### Пример

```
-> obj1.addElement(1, "hello");
-> obj1.addElement(2, "hi");
-> obj1.addElement(2, "hi");
--
<- После вызова obj1.printStructures()
<- 1 hello
<- 2 hi
```
