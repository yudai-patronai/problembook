from lib.testgen import TestSet
from lib.random import randint, randrange

RAND_TESTS_NUM = 20
MAX_RAND_NUM = 187
MAX_RAND_RANGE = 100

def rsa_decode(mess):
    mess_dec = []
    for el in mess:
        el_dec = el**107 % 187
        mess_dec.append(el_dec)
    return mess_dec

def get_case(mess):
  mess_dec = rsa_decode(mess)
  return ' '.join(map(str, mess)) + '\n', ' '.join(map(str, mess_dec)) + '\n'

tests = TestSet()

tests.add(*get_case([1, 2, 3, 4, 5]))
tests.add(*get_case([75]))

for _ in range(RAND_TESTS_NUM):
  M = randrange(MAX_RAND_RANGE)
  mess = [randint(MAX_RAND_NUM) for _ in range(M)]
  tests.add(*get_case(mess))
