def babyl2dec(babyl):
    # v = 1, < = 10
    # decimal = a0 * 60^0 + a1 * 60^1 + ... + an * 60^n

    power = 0
    dec = 0
    a_i = 0

    for b in reversed(babyl.split('.')):
        tens = b.count('<')
        ones = b.count('v')

        a_i = tens * 10 + ones
        dec += a_i * 60**power
        power += 1

    return dec

babyl = input()
print(babyl2dec(babyl))