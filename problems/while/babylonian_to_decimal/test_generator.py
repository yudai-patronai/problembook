from lib.testgen import TestSet

tests = TestSet()

def babyl2dec(babyl):
    # v = 1, < = 10
    # decimal = a0 * 60^0 + a1 * 60^1 + ... + an * 60^n

    power = 0
    dec = 0
    a_i = 0

    if not set(babyl) <= {'.', 'v', '<'}:
        print('Babyl contains illegal characters:', babyl)
        exit(1)

    for b in reversed(babyl.split('.')):
        tens = b.count('<')
        ones = b.count('v')

        # order of v and < is not checked

        if tens > 5:
            print('Wrong babyl:', babyl)
            print('Exceed number of "<" = {} at a_{}:'.format(tens, power))
            exit(1)

        if ones > 9:
            print('Wrong babyl:', babyl)
            print('Exceed number of "v" = {} at a_{}:'.format(tens, power))
            exit(1)

        a_i = tens * 10 + ones
        if a_i > 59:
            print('Wrong babyl:', babyl)
            print('a_{} = {} > 59'.format(power, a_i))
            exit(1)

        dec += a_i * 60**power
        power += 1

    return dec


babylons = [ # v = 1, < = 10, < must be first, then v
    '<<<<<vvvvvvv',
    'vv.',
    'vv..<vv',
    'v..',
    'vvvvvvvv.<<<<vvv.<<<vvvvv', # 31415
    'v.<vvvvv.<<<.<<vvvvvvvv', # 271828
    'v..<vv.',
]

for b in babylons:
    quest = b + '\n'
    ans = str(babyl2dec(b)) + '\n'
    tests.add(quest, ans)