---
id: c324a4ff-2b54-4caa-b7a6-d50d7654e642
longname: Как запомнить котов
languages: [cpp]
tags: [pointers]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Вам нужно написать две функции.
1. `Cat* get_home_for_a_cats_pride(unsigned int n)` выделяет память под массив из n котов - структур Cat. В качестве аргумента она принимает нужное количество элементов, а возвращает указатель на начало выделеной памяти.
2. `void clear_home_of_a_cats_pride(Cat *cats, unsigned int n)` корректно очищает эту память. В качестве единственного аргумента она принимает указатель на память, которая была выделена при помощи функции get_home_for_a_cats_pride.

Обратите внимание, что вам также надо выделить память под поле name. Считаем, что имя кота не длиннее 10 символов. 

Ответственность за корректный вызов этих функций в нужном порядке ложится на проверяющую программу. Это простая задача, вы можете не писать проверку корректности аргументов и прочую "защиту от дурака". Сосредоточьтесь на корректной работе с памятью.

Для проверки будет использоваться следующий код. Вы можете использовать его для отладки.

	#include <iostream>
	using std::cin;
	using std::cout;
	using std::endl;
	
	struct Cat {
	    char *name;
	    unsigned int id;
	    double weight, length;
	    unsigned int mice_caught;
	};
	
	Cat* get_home_for_a_cats_pride(unsigned int n);
	void clear_home_of_a_cats_pride(Cat *cats, unsigned int n);
	
	int main() {
	    unsigned int n;
	    cin >> n;
	    Cat *a = get_home_for_a_cats_pride(n);
	    for (int i = 0; i < n; i++) {
	        cin >> a[i].name >> a[i].weight >> a[i].length >> a[i].mice_caught;
	        a[i].id = i;
	    }
	    for (int i = 0; i < n; i++)
	        cout << a[i].name << " ";
	    cout << endl;
	    clear_home_of_a_cats_pride(a, n);
	    return 0;
	}

В проверяющую программу отправлять только функции `get_home_for_a_cats_pride` и `clear_home_of_a_cats_pride`.

Функцию `main` и все прочее отправлять не нужно.

### Формат входных данных

Число n - количество котов.
Вся необходимая информация о каждом коте - имя, вес, длина и количество мышей.

### Формат выходных данных

Имена котов в строку без пробелов.

### Примеры

```
-> 5
-> Lanfear 1.3 23.6 1000
-> Annoura 2.5 1.6 20
-> Atuan 1.6 0.6397 15
-> Leane 1.7 0.684 3
-> Liandrin 2.6 0.257 165
--
<- Lanfear Annoura Atuan Leane Liandrin 
```
