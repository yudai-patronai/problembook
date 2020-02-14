def poly_hash(p, m, s):

    h = 0
    for c in s:
        h = ( (h * p) % m + ord(c)) % m

    return h


def search(hash_table, element):
    length = len(hash_table)
    m = 10000
    p = 11
    hsh = poly_hash(p, m, element)
    index = hsh % length
    if len(hash_table[index]) == 0:
        return 'Value Not Found'
    lenchain = len(hash_table[index])
    for i in range(lenchain):
        if hsh == hash_table[index][i][0]:
            return hash_table[index][i][2]
    return 'Value Not Found'


print(search(hash_table1, input()))
