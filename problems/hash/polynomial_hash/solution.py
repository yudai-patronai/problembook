def poly_hash(p, m, s):
    # полиномиальный хеш справа-налево
    # строка s = s_0 s_1 .. s_i .. s_{n-1}
    # хеш =
    #  (o_0 * p^{len(s)-1} + o_1 * p^{len(s)-2} + ... + o_i * p^(len(s)-i-1) + ... + o_{n-2} * p + o_{n-1}) mod m
    #  где o_i = ord(s_i)

    h = 0
    for c in s:
        h = ( (h * p) % m + ord(c)) % m  # % m внутренний для избежания переполнения (длинной арифметики)

    return h

p, m = map(int, input().split())
s = input()

print(poly_hash(p, m, s))
