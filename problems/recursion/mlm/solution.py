def mlm(n):
    p = 0.3
    if n == 1:
        return 100*p + 10
    else:
        f = (1-p)*(mlm(n-1) - 10)/p
        return p*(100 + 2*f) + 10


if __name__ == '__main__':
    n = int(input())
    print(int(mlm(n)))
