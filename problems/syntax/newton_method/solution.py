def newton_method(f, d, x, eps=1e-4):
    yield (x, f(x))
    while True:
        if d(x):
            xn = x - f(x)/d(x)
        else:
            xn = x
        yield (xn, f(xn))
        if abs(f(xn)) <= eps:
            return
        x = xn
