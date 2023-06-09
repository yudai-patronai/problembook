
def table2dict(hash_table):
    # конвертирует таблицу из header.py в Dict
    d = dict()
    for chain in filter(lambda x: bool(x), hash_table): # непустые цепочки
        for elem in chain:
            _, key, value = elem
            d[key] = value
    return d

d1 = table2dict(hash_table)

key = input()
value1 = d1.pop(key, ERROR_MSG)
value2 = remove(hash_table, key)
d2 = table2dict(hash_table)

if d1.keys() != d2.keys():
    raise ValueError('Your remove(hash_table, key) function: 1) does not remove element OR 2) removes extra elements.')

print(value2)

