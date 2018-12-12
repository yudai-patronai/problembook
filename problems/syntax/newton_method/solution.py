def newton_method(f, d, x, eps=1e-4):
    yield (x, f(x))
    while True:
        xn = x - f(x)/d(x)
        yield (xn, f(xn))
        if abs(f(xn)) <= eps:
            return
        x = xn
