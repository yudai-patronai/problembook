---
id: 170af7c9-c358-4400-988a-906e3106d9bd
longname: Два коня
languages: [python]
tags: [graphs,bfs]
checker: cmp_int
time_limit: 1
real_time_limit: 5
max_vm_size: 64M
---


На стандартной шахматной доске (8х8) живут 2 шахматных коня: Красный и Зеленый. Обычно они беззаботно скачут по просторам доски, пощипывая шахматную травку, но сегодня особенный день: у Зеленого коня День Рождения. Зеленый конь решил отпраздновать это событие вместе с Красным. Но для осуществления этого прекрасного плана им нужно оказаться на одной клетке. Заметим, что Красный и Зеленый шахматные кони сильно отличаются от черного с белым: они ходят не по очереди, а одновременно,и если оказываются на одной клетке, никто никого не съедает. Сколько ходов им потребуется, чтобы насладиться праздником?

### Формат входных данных

На вход программы поступают координаты коней, записанные по стандартным шахматным правилам (т.е. двумя символами - маленькая латинская буква (от a до h) и цифра (от 1 до 8), задающие столбец и строку соответственно).

### Формат выходных данных

Требуется вывести наименьшее необходимое количество ходов, либо число -1, если кони не могут встретиться.

### Примеры

```
-> a1 a3
--
<- 1
```