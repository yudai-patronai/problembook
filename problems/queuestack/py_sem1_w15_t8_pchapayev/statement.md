

---
id: 3decf097-2ee7-419a-8987-f0d9698fb47b
longname: Покер Чапаева
languages: [ python]
tags: [queue,stack]
checker: cmp_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Василий Иванович придумал новый вид покера. Там каждый игрок должен собрать как можно больше карт в прикуп. Если у двух подряд приходящих карт совпадает масть, а достоинство отличается не больше, чем на 2  - их можно отправить в прикуп. И если достоинство карты в начале расклада совпадает с достоинством карты в конце, то эти две тоже можно отправить в прикуп. Сосчитать, сколько карт окажется в прикупе при данном порядке следования карт в игре. (Если Петька ни разу не зевнул).  

### Формат входных данных

Строка названий карт через пробел. Каждая карта - это буква из {a,b,c,d} и цифра от 0 до 9 (всего карт в колоде 36). 

### Формат выходных данных

Одно число — максимально возможное количество карт в прикупе.

### Примеры

```
-> a1 a2 b3 c9 d0
--
<- 2
```

```
-> a3 a2 a5 b5 c5
--
<- 4
```