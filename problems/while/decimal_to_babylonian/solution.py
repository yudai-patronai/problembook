def dec2babyl(num):
    # представление числа в вавилонской системе
    # decimal = a0 * 60^0 + a1 * 60^1 + ... + an * 60^n

    babyl = ''

    n = 0
    dec_ceil = 60
    while True:  # поиск ограничения сверху
        if dec_ceil > num:
            break
        else:
            n += 1
            dec_ceil += 59 * 60**n

    for i in range(n, -1, -1):
        a_i = num // (60 ** i)
        num -= a_i * 60**i

        babyl_a = '<' * (a_i // 10)
        babyl_a += 'v' * (a_i % 10)
        babyl += babyl_a
        if i != 0:
            babyl += '.'

    return babyl


dec = int(input())

print(dec2babyl(dec))
