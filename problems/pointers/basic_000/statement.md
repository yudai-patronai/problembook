---
id: d61100c0-131a-4783-96cc-b5059f412b83
longname: Указатели и адресная арифметика 000
languages: [cpp]
tags: [pointers]
checker: cmp_int_seq
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Вам нужно написать функцию, которая выводит на экран последовательность из шести целых чисел. Числа выводятся через пробел, в конце символ конца строки.

Для проверки будет использоваться следующий код. Вы можете использовать его для отладки. 

	#include <iostream>
	using std::cin;
	using std::cout;
	using std::endl;

	void print_array(int* p);

	int main() {
	    int a[6];
	    for (int i = 0; i < 6; i++)
		cin >> a[i];
	    print_array(a);
	    return 0;
	}

В проверяющую программу отправлять только функцию `print_array`.

Функцию `main` и все прочее отправлять не нужно.

### Формат входных данных

Последовательность целых чисел.

### Формат выходных данных

Ровно та же последовательность целых чисел.

### Примеры

```
-> 1 2 3 4 5 6
--
<- 1 2 3 4 5 6
```

