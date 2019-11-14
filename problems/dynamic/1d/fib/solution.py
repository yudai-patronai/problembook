def fib(n, external_start=True):
    if n <= 1:
        return 1
    global cache
    if external_start:
        cache = [None] * (n + 1)
        cache[:2] = 0, 0
    if cache[n] == None:
        cache[n] = fib(n - 2, False) + fib(n - 1, False)
    return cache[n]


print(fib(int(input())))
