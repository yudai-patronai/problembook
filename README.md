# problembook
Задачник по программированию.

## Использование contest.py

### Поиск задач

```
❯ ./contest.py find-problems

  #  Идентификатор                         Название                                                           Теги
---  ------------------------------------  -----------------------------------------------------------------  -----------------------
  1  8120e7d1-ddde-4996-b262-b5c9b3b55098  Построить остовное дерево обходом в ширину                         graphs bfs
  2  f47e0efe-913c-4f1c-acc2-7c4ca0297acf  Сильно связный ли орграф?                                          graphs connectivity dfs
  3  de2efbda-7f5f-4d9f-b59a-1284d7b949f6  Сильные и слабые компоненты связности                              graphs connectivity dfs
...
```

### Добавление задач

```
❯ ./contest.py create-problem -h
usage: contest create-problem [-h] -p PATH [-t TAGS] [-L {md}] [-l LONGNAME]
                              [-F FROM_XML]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Путь, по которому будет создана задача
  -t TAGS, --tags TAGS  Список тегов через запятую
  -L {md}, --markdown-language {md}
                        Язык разметки
  -l LONGNAME, --longname LONGNAME
                        Длинное название
  -F FROM_XML, --from-xml FROM_XML
                        Описание в задачи в xml для импорта
```

#### Создание задачи из шаблона

```
❯ ./contest.py create-problem -p graphs/dfs/acyclic -t grphs,dfs -l "Проверка ацикличности графа"
```

#### Создание задачи при помощи описания для ejudge в xml

```
❯ ./contest.py create-problem -p test/test -F /path/to/description.xml 
```

### Генерация тестов для всех задач в репозитории

```
❯ ./contest.py generate-tests -h
usage: contest generate-tests [-h] [-j JOBS] [-f]

optional arguments:
  -h, --help            show this help message and exit
  -j JOBS, --jobs JOBS  Количество параллельных потоков для генерации
  -f, --force-overwrite
                        Перезаписывать существующие тесты
```

```
❯ ./contest.py generate-tests -j4 -f
```

### Проверка корректности условий в репозитории

```
❯ ./contest.py validate -h
usage: contest validate [-h] [id]

positional arguments:
  id          Идентификатор задачи

optional arguments:
  -h, --help  show this help message and exit
```

#### Проверка для одной задачи

```
❯ ./contest.py validate 0f2d0de1-1bad-4d4b-a5db-b016df216d28
  #  Идентификатор                         Название                                Тесты    Генератор тестов    Решение    Контрольная сумма    Статус
---  ------------------------------------  --------------------------------------  -------  ------------------  ---------  -------------------  --------
  1  0f2d0de1-1bad-4d4b-a5db-b016df216d28  Поиск расстояния на прямоугольном поле  ✔️        ✔️                   ✖️          ?                    ✖️
```

#### Проверка для всех задач

```
❯ ./contest.py validate
  #  Идентификатор                         Название                                                           Тесты    Генератор тестов    Решение    Контрольная сумма    Статус
---  ------------------------------------  -----------------------------------------------------------------  -------  ------------------  ---------  -------------------  --------
  1  08e5d404-e27c-48b1-90f5-e8a4c037fa77  Восстановление кратчайшего пути при помощи алгоритма Дейкстры      ✔️        ✔️                   ✔️          ✔                    ✔️
  ...
  9  0f2d0de1-1bad-4d4b-a5db-b016df216d28  Поиск расстояния на прямоугольном поле                             ✔️        ✔️                   ✖️          ?                    ✖️
 ...
 21  ab46d419-f4bf-461b-8403-421a45fa6605  Нахождение вершины-"столицы"                                       ✔️        ✔️                   ✔️          ✔                    ✔️
```

### Просмотр информации о задаче

```
❯ ./contest.py info -h
usage: contest info [-h] id

positional arguments:
  id          Идентификатор задачи

optional arguments:
  -h, --help  show this help message and exit
```

```
❯ ./contest.py info c7ae1da3-e9e7-423b-9139-9d3245369aae
id: c7ae1da3-e9e7-423b-9139-9d3245369aae
Название: Кузнечик-брокер
Путь: ./problems/dynamic/1d/grasshopper_broker
```

### Просмотр описания задачи

```
❯ ./contest.py show --help
usage: contest show [-h] id

positional arguments:
  id          Идентификатор задачи

optional arguments:
  -h, --help  show this help message and exit
```

```
❯ ./contest.py show ce63db20-7666-466c-9084-b3cdae761b5b
---
id: ce63db20-7666-466c-9084-b3cdae761b5b
longname: Поиск длины кратчайшего пути при помощи алгоритма Дейкстры
tags: [graphs,dijkstra]
checker: cmp_file
...
```

### Редактирование задачи

```
❯ ./contest.py edit --help
usage: contest edit [-h] id

positional arguments:
  id          Идентификатор задачи

optional arguments:
  -h, --help  show this help message and exit
```

```
❯ ./contest.py edit ce63db20-7666-466c-9084-b3cdae761b5b
```

### Фиксация статуса задачи

```
❯ ./contest.py commit -h
usage: contest commit [-h] [-f] id

positional arguments:
  id                    Идентификаторы задач

optional arguments:
  -h, --help            show this help message and exit
  -f, --force-overwrite
                        Перезаписать контрольные суммы
```

```
❯ ./contest.py commit f47e0efe-913c-4f1c-acc2-7c4ca0297acf
```

### Создание контеста

```
❯ ./contest.py create-contest -h
usage: contest create-contest [-h] -n NAME [-f] problems [problems ...]

positional arguments:
  problems              Список идентификаторов задач

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Название контеста
  -f, --force-overwrite
                        Перезаписывать существующие конфиги контестов
```

```
❯ ./contest.py create-contest -n 900009 c7ae1da3-e9e7-423b-9139-9d3245369aae  9ce1b6ca-c82a-489e-a783-ecf78fa3c8f8d -f
```

### Генерация конфига для ejudge по описанию контеста

```
❯ ./contest.py ejudge --h
usage: contest ejudge [-h] -t TEMPLATE -o OUTPUT_DIR [-f] contest

positional arguments:
  contest               Файл с описание контеста

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE, --template TEMPLATE
                        Шаблон конфига
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Выходной путь
  -f, --force-overwrite
                        Перезаписывать существующие конфиги ejudge
```

```
❯ ./contest.py -v ejudge -t python3-ejudge.cfg.jinja2 -o /tmp contests/4_bfs_dijkstra.yml -f
```
