
---
id: 4004a602-98ea-4509-bd9f-0ca65a815e15
longname: Последствия эпидемии
languages: [cpp]
tags: [countsort]
checker: cmp_unsigned_int_seq
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


К вам попали данные мировых клиник о возрасте, течении болезни и исходе COROVA-вируса у 1.5 млн пациентов. Данные представлены в виде таблицы, где первый столбец — возраста пациентов, а второй — маркер: либо 0 (пациент умер), либо 1 (пациент болен), либо 2 (пациент излечился). Последняя строка таблицы имеет во втором столбце маркер «3», что означает конец таблицы.

Вам необходимо представить статистику о вероятности положительного исхода болезни в зависимости от возраста, игнорируя информацию о ещё больных на данный момент пациентах. Статистические данные необходимо представить в формате таблицы, где первый столбец — возраста из исследуемого диапазона, а второй — вероятность выздоровления в процентах.

### Формат входных данных

Таблица, на каждой строке по 2 числа через пробел. Последняя строка содержит число 3 на второй позиции.

### Формат выходных данных

Таблица по возрастам, отсортированная по возрастанию. Второй столбец - целое число вероятности выздоровления в процентах.
Проценты следует округлять до целого числа функцией round() математической библиотеки.

### Пример

```
-> 40 1
-> 32 2
-> 32 1
-> 50 2
-> 32 0
-> 60 0
-> 0 3
--
<- 32 50
<- 50 100
<- 60 0
```
