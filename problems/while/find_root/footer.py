func_str = input()
a, b, tol, true_root = [float(e) for e in input().split()]

eps = 1e-6
exec(func_str)
root = find_root(f, a, b, tol)

if abs(f(root)) < eps or abs(root - true_root) < tol:
    print('YES')
else:
    print('NO')
