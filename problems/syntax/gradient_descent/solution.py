def gradient_descent(f, d, x, lr=0.1, eps=1e-4):
    yield (x, f(x))
    while True:
        xn = x - lr*d(x)
        yield (xn, f(xn))
        if abs(f(xn) - f(x)) <= eps:
            return
        x = xn
        