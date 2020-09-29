---
id: 43c15d5b-5bb8-4c7f-8c6c-1b244c30e871
longname: Разделение скобочных последовательностей
languages: [cpp, python]
tags: [easy, strings]
checker: cmp_yesno
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Дана правильная скобочная последовательность (псп). Нужно вывести, на какое максимальное число правильных скобочных последовательностей её можно разбить.

Правильная скобочная последовательность здесь -- последовательность круглых скобок [s1, s2, ..., sn] такая, что количество левых и правых скобок в ней совпадает, и для любой подпоследовательности вида [s1, s2, ..., si], 1 <= i <= n число правых скобок не больше числа левых.

Например, строка (()()) является правильной скобочной последовательностью, а строки ((( и ())( не являются.

### Формат входных данных

Одна строка -- правильная скобочная последовательность длиной не больше 100 000 и не меньше 1 символа.

### Формат выходных данных

Одно число -- максимальное число правильных скобочных последовательностей, на которые можно разбить данную.

### Примеры

```
-> (()())
--
<- 1
```

```
-> ()(())()()
--
<- 4
```

### Пояснение

Строку ()(())()() можно разбить на 4 псп: (), (()), (), (). Строку (()()) нельзя разбить на несколько правильных скобочных последовательностей. 