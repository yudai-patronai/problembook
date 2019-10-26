def isans(n, a, b):
    return a**3 + b**3 == n


def number_cubic_decompose(n):
    num1 = 1
    num2 = 0
    ans = None, None
    while num1 ** 3 <= n:
        if isans(n, num1, num2):
            ans = num1, num2
            break
        elif isans(n, num1, 0):
            ans = 0, num1
            break
        else:
            num2 = num1
            while num2 ** 3 <= n:  # может быть оптимизировано?
                if isans(n, num1, num2):
                    ans = num1, num2
                    break
                else:
                    num2 += 1
        num1 += 1

    return ans


n = int(input())
a, b = number_cubic_decompose(n)

if a is None or b is None:
    print('impossible')
else:
    print(a, b)
