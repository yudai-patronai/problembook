def f(x):
    return x * x + x ** 0.5


def solve(c):
    left = 0
    right = c
    while True:
        m = (right + left) / 2
        y = f(m)
        if abs(y - c) < 1e-6:
            return m
        elif y > c:
            right = m
        else:
            left = m


x = float(input())
y = solve(x)
print("{:.06f}".format(y))
