# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-36.
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Популярная газета объявила конкурс на выбор лучшего фильма, для которого
стоит снять продолжение. На выбор читателей было предложено 10 фильмов.
Вам предлагается написать эффективную, в том числе и по используемой
памяти, программу, которая будет статистически обрабатывать результаты
sms-голосования по этому вопросу, чтобы определить популярность того или
иного фильма. Следует учитывать, что количество голосов в списке может
быть очень велико. На вход программе в первой строчке подается
количество пришедших sms-сообщений N. В каждой из последующих N строк
записано название фильма. Пример входных данных:
    6
    Белое солнце пустыни
    Бриллиантовая рука
    Белое солнце пустыни
    Белое солнце пустыни
    Гараж
    Бриллиантовая рука
Программа должна вывести список всех фильмов, встречающихся в списке, в
порядке убывания (невозрастания) количества отданных за них голосов с
указанием этого количества голосов. Название каждого фильма должно быть
выведено только один раз. Пример выходных данных для приведенных входных
данных:
    Белое солнце пустыни 3
    Бриллиантовая рука 2
    Гараж 1
"""
N = int(input())
cnt = {}
for i in range(N):
    title = input().rstrip()
    cnt[title] = cnt.get(title, 0) + 1

cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
for x in cnt:
    print(x[0], x[1])
