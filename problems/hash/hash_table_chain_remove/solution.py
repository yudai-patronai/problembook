ERROR_MSG = 'KeyError'

def poly_hash(p, m, s):
    h = 0
    for c in s:
        h = ( (h * p) % m + ord(c)) % m
    return h


def remove(hash_table, key):
    m = 100
    p = 91

    hsh = poly_hash(p, m, key)
    chain = hash_table[hsh % len(hash_table)]

    if len(chain) == 0:
        return ERROR_MSG
    
    for elem in chain:
        if hsh == elem[0] and key == elem[1]:
            value = elem[2]
            chain.remove(elem)
            return value

    return ERROR_MSG


