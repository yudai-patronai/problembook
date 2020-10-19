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
x_min, x_max = map(int, input().split())
y_min, y_max = map(int, input().split())

if a == 0 and b == 0:
    if c == 0:
        print((x_max - x_min + 1) * (y_max - y_min + 1))
    else:
        print(0)
    exit()
g, xg, yg = ext_euclid(a, b)
if c % g:
    print(0)
    exit()
x0 = xg * c//g
y0 = yg * c//g

kx_min = (x_min - x0) * g // b
kx_max = (x_max - x0) * g // b
ky_min = (y0 - y_max) * g // a
ky_max = (y0 - y_min) * g // a

if kx_min > ky_max or kx_max < ky_min:
    print(0)
    exit()
if ky_min <= kx_min <= ky_max:
    print(min(ky_max, kx_max) - kx_min + 1)
else:
    print(min(ky_max, kx_max) - ky_min + 1)
