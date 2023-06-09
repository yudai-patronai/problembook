---
id: 24255517-2759-4c19-a5a7-5e6d7888d8a7
longname: Статистика потока пациентов
languages: [cpp,python]
tags: [while,float]
checker: cmp_double
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Главный врач хочет проанализировать статические данные потока поступающих пациентов.
Он хочет увидеть среднюю арифметическую температуру пациентов от 60 лет и выше, а также пациентов, вес которых отклоняется от нормального больше, чем на 10 килограмм. Нормальным весом в килограммах считать рост за вычетом ста сантиметров. Если таких пациентов нет - вывести ноль.

### Формат входных данных

На вход алгоритм получает количество строк N, а затем N строк.
В каждой строке по 4 числа, разделённых табуляцией: age height weight temperature

### Формат выходных данных

Одно вещественное число. Точность проверки - 5 знаков после запятой.


### Примеры

```
-> 3
-> 17 180 90 37.6
-> 62 170 70 38.2
-> 40 160 60 36.9
--
<- 38.2
```

```
-> 3
-> 17 180 60 37.1
-> 29 174 85 39.1
-> 40 160 50 36.9
--
<- 38.1
```

```
-> 3
-> 10 130 30 37.6
-> 65 170 70 38.4
-> 40 160 52 38.2
--
<- 38.4
```

```
-> 5
-> 32 170 250 37.3
-> 20 150 200 37.5
-> 34 170 70 38.9
-> 57 155 60 37.5
-> 45 160 65 36.5
--
<- 37.4
```

```
-> 2
-> 32 170 70 37.3
-> 20 160 65 37.5
--
<- 0
```

