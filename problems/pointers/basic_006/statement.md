---
id: fa5fb9bb-0a13-4a7c-b5ed-12c065677f6b
longname: Подсчет мышей
languages: [cpp]
tags: [pointers]
checker: cmp_unsigned_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Вам нужно написать функцию `unsigned int count_total_mice_amount(Cat* cats, unsigned int n)`, которая считает общее количество мышей, пойманных котами - возвращает сумму полей mice_caught элементов массива структур Cat. В качестве аргумента она принимает указатель на начало массива и количество элементов в нем. 

Для проверки будет использоваться следующий код. Вы можете использовать его для отладки.

	#include <iostream>
	using std::cin;
	using std::cout;
	using std::endl;
	
	struct Cat {
	    char name[20];
	    unsigned int id;
	    double weight, length;
	    unsigned int mice_caught;
	};
	
	unsigned int count_total_mice_amount(Cat* cats, unsigned int n);
	
	int main() {
	    unsigned int n;
	    cin >> n;
	    Cat *a = new Cat[n];
	    for (int i = 0; i < n; i++) {
	        cin >> a[i].name >> a[i].weight >> a[i].length >> a[i].mice_caught;
	        a[i].id = i;
	    }
	    cout << count_total_mice_amount(a, n) << endl;
	    delete[] a;
	    return 0;
	}

В проверяющую программу отправлять только функцию `count_total_mice_amount`.

Функцию `main` и все прочее отправлять не нужно.

### Формат входных данных

Число n - количество котов.
Вся необходимая информация о каждом коте - имя, вес, длина и количество мышей.

### Формат выходных данных

Сумма всех пойманных мышей.

### Примеры

```
-> 5
-> Lanfear 1.3 23.6 1000
-> Annoura 2.5 1.6 20
-> Atuan 1.6 0.6397 15
-> Leane 1.7 0.684 3
-> Liandrin 2.6 0.257 165
--
<- 1203
```

