def poly_hash(p, m, s):
    h = 0
    for c in s:
        h = ( (h * p) % m + ord(c)) % m
    return h


def search(hash_table, key):
    m = 100
    p = 91

    hsh = poly_hash(p, m, key)
    chain = hash_table[hsh % len(hash_table)]

    if len(chain) == 0:
        return ERROR_MSG
    
    lenchain = len(chain)
    for elem in chain:
        if hsh == elem[0] and key == elem[1]:
            return elem[2]
    
    return ERROR_MSG

