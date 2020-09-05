m = None

while True:
    x = input()
    if x == '#':
        break

    x = int(x)
    if m is None or x > m:
        m = x

print(m)
