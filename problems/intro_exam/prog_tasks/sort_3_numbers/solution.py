a = int(input())
b = int(input())
c = int(input())

if a >= b:
    if b >= c:
        print(c, b, a)
    else:
        if a >= c:
            print(b, c, a)
        else:
            print(b, a, c)
else:
    if b <= c:
        print(a, b, c)
    else:
        if a <= c:
            print(a, c, b)
        else:
            print(c, a, b)
