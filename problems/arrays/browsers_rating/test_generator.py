from lib.testgen import TestSet
from lib.random import randint

brows = ('Netscape Navigator\n', 'Opera\n', 'Google Chrome\n', 'Internet Explorer\n', 'Word\n')

def calc_answer(lst):
    res = ''
    blist = {}
    for i in range(len(lst)):
        blist[lst[i]] = blist.get(lst[i], 0) + 1
    blist = sorted(blist.items(), key = lambda x: x[1], reverse = True)
    i = 0
    snum = 0
    for x in blist:
        i += 1
        if snum < i:
            pcnt = 0
            for y in blist:
                if y[1] == x[1]:
                    pcnt += 1
            snum += pcnt
            if pcnt == 1:
                nsamp = str(i)
            else:
                nsamp = str(i) + " - " + str(i + pcnt - 1)
        res += nsamp + ' ' + brows[x[0]]
    return res


def gen_answer(l1, l2):
    res = ''
    if len(l1) > 0:
        res += 'desktop browsers rating\n'
        res += calc_answer(l1)
    if len(l2) > 0:
        res += 'mobile browsers rating\n'
        res += calc_answer(l2)
    return res


tests = TestSet()

q1 = '6\ndesktop Netscape Navigator\ndesktop Opera\ndesktop Google Chrome\n' +\
    'mobile Opera\ndesktop Google Chrome\nmobile Google Chrome\n'
a1 = 'desktop browsers rating\n1 Google Chrome\n2 - 3 Netscape Navigator\n' +\
    '2 - 3 Opera\nmobile browsers rating\n1 - 2 Opera\n1 - 2 Google Chrome\n'
tests.add(q1, a1)
q1 = '3\ndesktop Opera\ndesktop Opera\ndesktop Opera\n'
a1 = 'desktop browsers rating\n1 Opera\n'
tests.add(q1, a1)

l1 = []
l2 = []
q1 = '40\n'
for cnt in range(40):
    i1 = randint(1, 100) % 2
    q1 += 'desktop ' if i1 == 0 else 'mobile '
    i2 = randint(1, 100) % 5
    q1 += brows[i2]
    if i1 == 0:
        l1.append(i2)
    else:
        l2.append(i2)
tests.add(q1, gen_answer(l1, l2))

    
