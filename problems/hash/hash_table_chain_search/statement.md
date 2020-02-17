---
id: a8afc600-b11f-4ec3-801f-47f053188bb9
longname: Ассоциативный массив на хеш-таблице с цепочками - Поиск элемента
languages: [python]
tags: [hash,standart]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Эта задача из серии по реализации ассоциативного массива на хеш-таблице с использованием цепочек для разрешения коллизий.

В задаче необходимо написать алгоритм поиска элемента по ключу.

В тестах вашей программе будет **доступна** хеш-таблица следующего формата:

```

hash_table = [
    [], # это пустая цепочка
    [[hash1, key1, value1]], # это цепочка с одним значением
    [[hash2, key2, value2], [hash3, key3, value3]], # это цепочка с двумя значениями
    ...
]

```

Она **хранится** в переменной `hash_table` (ввод таблицы осуществлять не нужно).
Размер таблицы 10.
Ключи и значения в таблице хранятся в виде строк.

Хеши в таблице получали с помощью полиномиальной хеш-функции с параметрами:
- основание 91
- модуль 100

Вам необходимо реализовать функцию-интерфейс `search(table, key)`, осуществляющую поиск элемента по ключу.

### Аргументы

Функция `search(table, key)` имеет два аргумента:
- table - хеш-таблица формата, как выше
- key - ключ, по которому осуществляется поиск (имеет тип `str`)

### Возвращаемое значение

Функция возвращает значение, лежащее по ключу `key`.
Если ключа нет, то функция должна вернуть строку `'KeyError'`.

### Примеры работы функции

Таблица:

```

example_table = [
    [], [],
    [
      [32, 'ONLY', 'pal;cw'],
      [62, 'INDUSTRY', 'lfow'],
      [72, 'LETRASET', 'awdwad'],
      [32, 'BEEN', 'lkawdk']
    ],
    [], [], [], [], [], [], [],
]

```

```
-> search(example_table, 'BEEN')
--
<- 'lkawdk'
```

```
-> search(example_table, 'PRODUCT')
--
<- 'KeyError'
```