---
id: 23cc4981-b8bd-4f9a-8e63-8f5d292d80d7
longname: Путешествие по лабиринту
languages: [cpp]
tags: [while,pointer]
checker: cmp_yesno
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Вы находитесь на плоском лабиринте локаций. Вам требуется найти медицинский центр со свободными койками.
Учтите, что свободные койки могут быть и в заведениях, не являющимися мед.центрами.
Карта дана вам в формате многосвязной структуры данных с указателями, базовым звеном которой является тип `Location_t`:

    enum Direction {
        UP = 0,
        DOWN = 1,
        RIGHT = 2,
        LEFT = 3
    };

    struct Location_t {
        bool is_medical_center;
        int free_beds;
        int indicator;
        struct Location_t *up;
        struct Location_t *down;
        struct Location_t *right;
        struct Location_t *left;
    };

Индикатор направления на локации показывает каким из четырёх указателей следует воспользоваться, чтобы попасть в следущую локацию.
Учтите, что некоторые из указателей могут равняться nullptr, что означает стену, непроходимость.

Вам нужно написать только функцию поиска. Описывать типы и создавать функцию `main()` не нужно!

    Location_t *find_medical_center(Location_t *start_location);



### Формат входных данных

Два числа, которые нужно сложить.

### Формат выходных данных

Одно число — результат.

### Примеры

```
-> 1 2
--
<- 3
```

```
-> 1 -1
--
<- 0
```
