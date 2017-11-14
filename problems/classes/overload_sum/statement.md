---
id: 68492a33-01b9-4115-93e5-a0eecf40480e
longname: Перегрузка оператора суммы
languages: [cpp]
tags: [classes]
source_header: header.cpp
source_footer: footer.cpp
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Добавьте в предыдущей задаче (Класс с массивом структур) перегруженный оператор суммы += , который соединяет массив
структур класса слева с массивом стуктур класса справа. Если элементы второго класса совпадают с элементами первого - они не добавляются. 

### Формат входных данных

Число и строка, разделенные пробелом

### Формат выходных данных

Элементы суммарного массива, где на каждой строчке выводится число и строка, разделенные пробелом

### Примеры

```
-> MyClass obj1;
-> obj1.addElement(1, "hi");
-> obj1.addElement(2, "hello");
-> obj1.addElement(2, "hello");
-> MyClass obj2;
-> obj2.addElement(3, "hey");
-> obj2.addElement(4, "pop");
-> obj2.addElement(2, "hello");
-> obj2.addElement(5, "hello");
-> obj1 += obj2;
-> obj1.printStructures();
--
<- 1 hi
<- 2 hello
<- 3 hey
<- 4 pop
<- 5 hello
```

