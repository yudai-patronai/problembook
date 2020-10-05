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


a, b, c = map(int, input().split())
if a == 0 and b == 0:
    if c == 0:
        print(1, 1)
    else:
        print("No solution")
    exit()
g, xg, yg = ext_euclid(a, b)
if c % g:
    print("No solution")
    exit()
print(xg + c//g, yg + c//g)
