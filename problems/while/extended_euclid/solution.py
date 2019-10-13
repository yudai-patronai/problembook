a, b = input().split()
a = int(a)
b = int(b)

def ext_euclid(a, b):
    x = 1
    y = 0
    qs = []
    while b != 0:
        r = a % b
        q = a // b
        qs.append(q)
        a = b
        b = r
    for q in qs[::-1]:
        buf = y
        y = x - y * q
        x = buf
    return a, x, y

print('{} {} {}'.format(*ext_euclid(a, b)))