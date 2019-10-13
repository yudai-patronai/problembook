def maya2dec(maya):
    sign_one = '.'
    sign_five = '|'

    pow = 0
    base = 20
    dec = 0
    for numeral in reversed(maya.split()):
        dec_part = numeral.count(sign_one) + 5 * numeral.count(sign_five)
        dec += dec_part * base**pow
        pow += 1

    return dec

maya = input()
print(maya2dec(maya))