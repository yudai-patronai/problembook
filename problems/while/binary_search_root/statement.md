---
id: 331db3b5-e3b3-499f-abda-3f8113d37442
longname: Двоичный поиск корня уравнения.
languages: [cpp]
tags: [binsearch,float]
checker: cmp_yesno
time_limit: 1
real_time_limit: 1

max_vm_size: 64M
---


Реализовать функцию,  реализующую поиск на интервале (a,b) корня x0 уравнения f(x) = 0 методом двоичного поиска (бисекции).

`double find_root(double (*f)(double), double a, double b, double tolerance)`

Точность определения `x0` не должна превышать значение `tolerance`.
Выполнение равенства `f == 0` проверять с невязкой `eps = 1e-6`.
Гарантируется наличие единственного корня на рассматриваемом интервале. Функция f непрерывна и имеет значения разных знаков на концах интервала (a, b).

### Аргументы функции

- `f` — `function` функция, нуль которой нужно найти
- `a` —левый край интервала поиска корня
- `b` — `float` правый край интервала поиска корня
- `tol` — `float` точность локализации корня уравнения f(x) = 0

### Возвращаемое значение

Одно число — найденный корень уравнения f(x) = 0.
