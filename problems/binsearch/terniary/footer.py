
f = eval("lambda x: {}".format(input()))
dx = eval("lambda x: {}".format(input()))
x = float(input())
lr = float(input())
eps = float(input())

if lr != 0.:
    xi, fxi = gradient_descent(f, dx, x, lr, eps)
    print("{:10.5}{:10.5}".format(xi, fxi))
else:
    xi, fxi = gradient_descent(f, dx, x)
    print("{:10.5}{:10.5}".format(xi, fxi))
