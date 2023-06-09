---
fixme: true
id: c830c75e-bbbe-492d-a43c-08d6216c1a06
longname: Реформа округов
tags: [graphs,dijkstra]
languages: [python]
time_limit: 1
real_time_limit: 5
max_vm_size: 64M
---

Правитель Графландии решил провести реформу административных округов в своём государстве.
Новые окружные центры правитель выбрал, вам остаётся всего лишь распределить остальные города по округам.

При этом правителю хочется, чтобы расстояние от города до окружного центра этого города не превышало расстояний от данного города до других окружных центров.

Если есть несколько вариантов расстановки - подойдет любой.
Если не справитесь, вам отрубят голову.

### Формат входных данных

На вход программе в первой строке подаётся несколько (не менее трёх) чисел через пробел: `N M CA CB ...`, где

- `2 ≤ N ≤ 1000` - число городов в государстве;
- `1 ≤ M ≤ 100000` - число дорог между городами;
- `Ci` - номера городов, которые правитель выбрал окружными центрами.

В следующих `M` строках задаются дороги, по три числа в каждой строке - номера соединенных городов и длина дороги.

Города нумеруются с нуля.

### Формат выходных данных

Для каждого города в отдельной строке выведите номер его окружного центра.
Для 0-го города - в первой строке, для 1-го - во второй и так далее, всего `N` строк.
Если для города не достижим ни один из окружных центров - выведите в соответствующей строке -1.

### Примеры

```
-> 4 3 0 1
-> 0 1 34
-> 2 1 7
-> 3 2 85
--
<- 0
<- 1
<- 1
<- 1
```

```
-> 6 5 0 1
-> 2 1 24
-> 4 2 1
-> 1 0 78
-> 5 1 51
-> 0 3 19
--
<- 0
<- 1
<- 1
<- 0
<- 1
<- 1
```
