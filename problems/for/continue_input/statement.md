---
id: b1826419-c4aa-4199-8971-5c8854cfdce7
longname: Непрерывный (CONTINUous) ввод
languages: [python]
tags: [for]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

В программу непрерывно вводятся строки. Ввод осуществляется до тех пор, пока либо новая строка не совпадет с предыдущей, либо новая строка не окажется пустой. Строки, которые  начинаются с заглавных букв нужно пропускать. 

Среди строк, которые удовлетворяют условию, нужно запомнить первую и последнюю букву, и напечатать все эти буквы слитно в одну строку.

### Формат входных данных

Вводится N(N не более 1000) строк. N заранее неизвестно. Напечатать на экран первые и последние буквы строк, удовлетворяющих условию выше. В строках могут встречаться нижние и заглавные английские буквы, цифры, а так же string.punctuation.

### Формат выходных данных

Строка, склеенная из первых и последних букв введенных строк.

### Примеры

```
-> 'Who is a good boy?'
-> 'mipt'
-> '777'
-> 'iddqd idkfa idclip'
-> '- Good'
-> ''
--
<- 'mt77ip-d'
```

```
-> 'a'
-> 'phystech2'
-> 'phystech2'
--
<- 'aap2'
```