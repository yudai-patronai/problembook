def rem2maya(x):  # строит разряд
    if x == 0:
        return '@'
    else:
        return '.' * (x % 5) + '|' * (x // 5)

def dec2maya(x):
    power = 1
    maya = ''
    while x != 0:
        rem = (x // power) % 20
        x -= rem * power
        power *= 20
        maya_rem = rem2maya(rem)
        maya = maya_rem + ' ' + maya if maya else maya_rem
    return maya

print(dec2maya(int(input())))
