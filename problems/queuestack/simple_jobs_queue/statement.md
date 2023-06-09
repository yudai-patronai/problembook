---
id: df2f613d-c9e3-41bc-9033-0fd2a444f255
longname: Очередь процессов
languages: [python]
tags: [easy,queue]
checker: cmp_int_seq
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Пользователь компьютера запускает несколько процессов. Процессы обозначаются целыми числами и одновременно на компьютере может исполняться только один.

Например, такая последовательность `3 → 2 → 4` означает выполнение процесса 3, затем процесса 2, а затем процесса 4.

Однако процессы, запускаемые пользователем являются комплексными. То есть, для их исполнения может потребоваться вызов некоторых других процессов в известной компьютеру последовательности. Эту задачу берёт на себя компьютер, незаметно для пользователя.

Например, такая *иерархия вызовов* `1 ← 3 ← 4 ← 2` означает, что

- процесс 1 является *атомарным*, он не требует вызова других процессов
- для исполнения процесса 3 требуется сначала исполнить процесс 1, и только потом процесс 3
- для исполнения процесса 4 требуется исполнить процесс 1, затем 3, и только потом процесс 4
- для исполнения процесса 2 требуется исполнить процессы 1, 3, 4 и только потом исполнить процесс 2

Вам необходимо написать программу, которая вычисляет очередь процессов с точки зрения компьютера, т.е., учесть иерархию вызовов.

Для данного примера ответом будет `1 → 3 → 1 → 3 → 4 → 2 → 1 → 3 → 4`.

### Примечание

Воспользуйтесь очередью `deque` для решения этой задачи.

    from collections import deque

### Формат входных данных

Всего две строки. В первой через пробел целые числа - последовательность процессов, запускаемых пользователем. Во второй строке в том же формате даётся иерархия вызовов.

### Формат выходных данных

Одна строка из целых чисел через пробел - очередь процессов с точки зрения компьютера. 

### Примеры

```
-> 3 2 4
-> 1 3 4 2
--
<- 1 3 1 3 4 2 1 3 4
```

```
-> 8 2 3 9
-> 4 2 9 3 8
--
<- 4 2 9 3 8 4 2 4 2 9 3 4 2 9
```

```
-> 15
-> 73 82 41 2 15 8 21
--
<- 73 82 41 2 15
```