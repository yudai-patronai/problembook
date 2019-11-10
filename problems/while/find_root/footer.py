

#''' # ЭТО не комментарий, а конец переменной source_code из header


exec(source_code)  # объект find_root(f, a, b, tol) становится доступным

func = input()
a, b, tol = [float(e) for e in input().split()]
eps = 1e-6

exec(func)

root = find_root(f, a, b, tol)

print(root)
