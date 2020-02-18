from lib.testgen import TestSet
from header import hash_table, ERROR_MSG


def table2dict(hash_table):
    # конвертирует таблицу из header.py в Dict
    d = dict()
    for chain in filter(lambda x: bool(x), hash_table): # непустые цепочки
        for elem in chain:
            _, key, value = elem
            d[key] = value
    return d

def question(key):
    return '{}\n'.format(key)

def answer(val):
    return '{}\n'.format(val)

# ключи, которые есть в header.hash_table и которых там нет (NONE-like строки)
keys = ['REMAINING', 'WAS', 'NoNE', 'NoneEE', 'EVER', 'SOFTWARE', '3NONE']
dict_from_hashtable = table2dict(hash_table)

tests = TestSet()
for k in keys:
    if k in dict_from_hashtable.keys():
        ans = dict_from_hashtable[k]
    else:
        ans = ERROR_MSG

    tests.add(question(k), answer(ans))
