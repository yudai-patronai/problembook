from math import sqrt

if __name__ == "__main__":
    eps = 1e-6
    a1, b1, c1 = [int(e) for e in input().split()]
    a2, b2, c2 = [int(e) for e in input().split()]
    d = a1 * b2 - b1 * a2
    if abs(d) < eps:
        print('NO')
    else:
        x = (b1 * c2 - c1 * b2) / d
        y = -(c2 + a2 * x) / b2
        print(round(x), round(y))
