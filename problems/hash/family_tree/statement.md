---
id: f494ca09-f55b-489b-8890-571933da9475
longname: Генеалогическое дерево
languages: [python]
tags: [dict,tree]
checker: cmp_yesno
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


В этой задаче в словаре `tree` содержится информация о генеалогическом дереве некоторой семьи.

Словарь хранит имена детей и родителей. Ключом является имя ребёнка, а значением — множество (`set`) имён родителей этого ребёнка.

Например, по такому словарю

    tree = {
        'C': {'A', 'B'},
        'F': {'C'},
        'D': {'C'},
    }

Можно определить, что родителями `C` являются `A` и `B`. А у `F` и `D` известен только один родитель — `C`.

В этой задаче необходимо написать пять функций, работающих с подобно устроенным словарём:

- `parents(tree, name)` - возвращает множество `set` родителей `name`;
- `grandparents(tree, name)` - возвращает множество `set` "дедушек и бабушек" `name`;
- `children(tree, name)` - возвращает множество `set` детей `name`;
- `grandchildren(tree, name)` - возвращает множество `set` "внуков и внучек" `name`;
- `siblings(tree, name)` - возвращает множество `set` "родных братьев и сестёр" `name`;

Если информация о "родственниках" в `tree` не известна, то указанные функции должны возвращать пустое множество `set()`.

В качестве решения отправьте код требуемых пяти функций.

### Примеры работы функций

    >>> tree = {
    ...     'C': {'A', 'B'},
    ...     'F': {'C'},
    ...     'D': {'C'},
    ... }
    >>> parents(tree, 'C')
    {'B', 'A'}
    >>> parents(tree, 'A')
    set()
    >>> grandparents(tree, 'D')
    {'B', 'A'}
    >>> grandparents(tree, 'C')
    set()
    >>> children(tree, 'A')
    {'C'}
    >>> children(tree, 'D')
    set()
    >>> grandchildren(tree, 'A')
    {'F', 'D'}
    >>> grandchildren(tree, 'F')
    set()
    >>> siblings(tree, 'F')
    {'D'}
    >>> siblings(tree, 'C')
    set()