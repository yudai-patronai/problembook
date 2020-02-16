---
id: f0c10292-b21d-4ecd-a156-e34d291fabb7
longname: Словарь со стандартными значениями (строки)
languages: [python]
tags: [for]
checker: cmp_int
time_limit: 1
real_time_limit: 1
source_header: header.py
source_footer: footer.py
max_vm_size: 64M
---

Необходимо реализовать класс PrefixClass, который будет обеспечивать следующую работу defaultdict в зависимости от переменной PREFIX, которая передана в конструктор.

```
class PrefixClass(object):
    # your code here
    pass

PREFIX = True
pc = PrefixClass(PREFIX)
dct = defaultdict(pc)

elems = [9, 3, 1, 3, 4, 10]

elems = [9, 3, 1, 3, 4, 10]
assert [dct[elem] for elem in elems] == ['>>1>>', '>>2>>', '>>3>>', '>>2>>', '>>4>>', '>>5>>']

pc.PREFIX = False
elems = [7, 3, 1, 5, 5]
assert [dct[elem] for elem in elems] == ['', '>>2>>', '>>3>>', '', '']

```

Код должен работать следующим образом:
Когда в словаре появляется новый ключ, то значение по умолчанию задается следующим образом:
1. Если переменная выставлена как PREFIX = False, то значением по умолчанию является пустая строка.
2. Если переменная выставлена как PREFIX = True, то значением по умолчанию является строка вида >>{}>> , где вместо скобок выставляется порядковый номер нового ключа.

Необходимо реализовать ТОЛЬКО класс PrefixClass без дополнительных элементов кода.

### Примеры работы с классом

```
pc.PREFIX = True
elems = [9, 3, 1, 3, 4, 10]
assert [dct[elem] for elem in elems] == ['>>1>>', '>>2>>', '>>3>>', '>>2>>', '>>4>>', '>>5>>']

pc.PREFIX = False
elems = [7, 3, 1, 5, 5]
assert [dct[elem] for elem in elems] == ['', '>>2>>', '>>3>>', '', '']
```

```
pc.PREFIX = True
elems = [1, 1, 2, 3]
assert [dct[elem] for elem in elems] == ['>>1>>', '>>1>>', '>>2>>', '>>3>>']

pc.PREFIX = False
elems = [4, 4, 5]
assert [dct[elem] for elem in elems] == ['', '', '']


pc.PREFIX = True
elems = [5, 6, 7]
assert [dct[elem] for elem in elems] == ['', '>>6>>', '>>7>>']
```
