f = eval("lambda x: {}".format(input()))
dx = eval("lambda x: {}".format(input()))
x = float(input())
eps = float(input())

if eps != 0.:
    for i, (xi, fxi) in enumerate(newton_method(f, dx, x, eps)):
        print("{}{:10.5}{:10.5}".format(i, xi, fxi))
else:
    for i, (xi, fxi) in enumerate(newton_method(f, dx, x)):
        print("{}{:10.5}{:10.5}".format(i, xi, fxi))
