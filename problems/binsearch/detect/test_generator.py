from lib.testgen import TestSet

def case(minv, maxv, zerov, minc, maxc, typ):
    maxv2 = maxv
    maxc2 = maxc
    
    minv ^= 0xbeef
    maxv ^= 0xbeef
    zerov ^= 0xbeef
    minc ^= 0xbeef
    maxc ^= 0xbeef
    
    return f"{minv} {maxv} {zerov} {minc} {maxc} {typ}", f"{maxv2} {maxc2}"

tests = TestSet()

tests.add(*case(110000,    130000,    120000,   39,  215, 167))
tests.add(*case(30563,     50216,     41749,    94,  286, 218))
tests.add(*case(217000,    217200,    217100,   17,  49,  429))
tests.add(*case(80546,     81927,     81018,    310, 337, 625))
tests.add(*case(19854,     25419,     20205,    219, 47,  172))
tests.add(*case(46518,     52281,     51307,    180, 270, 91))
tests.add(*case(110000,    130000,    120000,   355, 358, 218))
tests.add(*case(11000000,  13000000,  12000000, 357, 354, 167))

