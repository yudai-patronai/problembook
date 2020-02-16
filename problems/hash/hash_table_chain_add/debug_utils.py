"""
Ассоциативный массив на хеш-таблице с цепочками.

hash_table = [
    [],  # пустой элемент 
    # цепочка
    [[full_hash1, key1, value1], [full_hash2, key2, value2]], 
    ...
]
"""

HASH_MODULE = 100
HASH_BASE = 91
HTABLE_SIZE = 10

def poly_hash(p, m, s):
    """
    Полиномиальный хеш справа-налево, реализация из hash/polynomial_hash/
    """
    h = 0
    for c in s:
        h = ( (h * p) % m + ord(c)) % m
    return h

def insert(table, key, value):
    key_hash = poly_hash(HASH_BASE, HASH_MODULE, key)
    chain = table[key_hash % len(table)]

    # проверяем вхождение key, если есть, то перезапись
    for elem in chain:
        h, k, _ = elem
        if h == key_hash and k == key: # вычисление ленивое, проверка на ключ будет только при совпадении хешей
            elem[2] = value
            return

    # ключа в таблице нет
    chain.append([key_hash, key, value])

def print_table(table):
    # печать ответа
    for i, chain in enumerate(table):
        if not chain:
            continue
        print(i)
        for elem in chain:
            print(*elem)


hash_table = [[] for _ in range(HTABLE_SIZE)]

# with open('collision_test.txt') as f:
#     N = int(next(f))
#     for row in f:
#         k, val = row.split()
#         insert(hash_table, k, val)

s = """3
PHYSICS thermodynamics
INFORMATICS network_architecture
MATH number_theory
"""

for row in s.strip().split('\n')[1:]:
    print(repr(row))
    k, v = row.split()
    insert(hash_table, k, v)

print_table(hash_table)
# N = int(input())
# for _ in range(N):
#     key, value = input().split()
#     insert(hash_table, key, value)


