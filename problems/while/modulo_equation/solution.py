def ext_euclid(a, b):
    x = 1
    y = 0
    qs = []
    while b != 0:
        q, r = divmod(a, b)
        qs.append(q)
        a, b = b, r
    for q in reversed(qs):
        x, y = y, x - y * q
    return a, x, y

def solve_modulo_eq(m, a, b):
    if a < 0:
        b = -b
        a = -a
    g, x0, k0 = ext_euclid(a, m)
    if b % g != 0:
        return False
    dx = m // g
    x1 = x0 * (b // g)
    solutions = [x1 % m]
    split = 0
    for k in range(1, g):
        xk = solutions[k - 1] + dx
        solutions.append(xk % m)
        if split == 0 and xk >= m:
            split = k
    return solutions[split :] + solutions[: split]


m = int(input())
a = int(input())
b = int(input())

solutions = solve_modulo_eq(m, a, b)
if not solutions:
    print(-1)
else:
    print(*solutions)
