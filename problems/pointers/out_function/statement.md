---
id: b04c06de-39db-4e9a-87ca-35712244145a
longname: Написать функцию вывода
languages: [cpp]
tags: []
checker: cmp_file
time_limit: 1
source_header: header.cpp
real_time_limit: 1
max_vm_size: 64M
---


Написать функцию `void print_no_space(char* text)`, выводящую `text` строчными буквами без пробельных символов.

Признак конца строки - символ с кодом 0.

Использовать `int`, `float` и подобные запрещено. Пользуйтесь адресной арифметикой.

### Формат входных данных

Текст.

### Формат выходных данных

Текст без пробелов.

### Примеры

```
->   Hello vasia,     how are you?  
--
<- hellovasia,howareyou?
```

