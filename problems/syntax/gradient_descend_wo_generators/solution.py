def gradient_descent(f, d, x, lr=0.1, eps=1e-4):
    while True:
        xn = x - lr*d(x)
        if abs(f(xn) - f(x)) <= eps:
            return (xn, f(xn))
        x = xn
