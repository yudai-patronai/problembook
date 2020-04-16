import random
import sys
from itertools import chain, combinations

from lib.testgen import TestSet


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def gcd(a, b):
    while(b): 
       a, b = b, a % b
    return a 

def solv(st):
    def check(one):
        return 1 if (sum(gcd(a, b) for a in one for b in one) == len(one) * len(one) - len(one) + sum(one)) else 0
    
    return sum(check(one) for one in powerset(st))

tests = TestSet()

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# 1. Simple tests
tests.add('3\n2 3 5', '8')
tests.add('1\n2', '2')
tests.add('1\n3', '2')
tests.add('2\n2 4', '3')

# 2. Edge case for some implementations
tests.add('1\n1', '2')

# 3. All-are-primes tests
for N in range(5, 25, 2):
    random.shuffle(primes)
    tests.add("{0}\n{1}".format(N, " ".join(map(str, primes[:N]))), str(2**N))
    
# 4. Generic tests   
for i in range(15):
    print(f"[+] Na-even rand {i}")
    N = random.randrange(17, 20)
    numbers = [random.randrange(1001, 10000, 2) for _ in range(N)]
    ans = solv(numbers)
    tests.add("{0}\n{1}".format(N, " ".join(map(str, numbers))), str(ans))
    
# 5. Big tests
tests.add("24\n3243 3175 8717 2985 8989 7777 4247 3265 6963 9291 8789 9073 7225 7247 2591 7113 3461 9999 9563 5351 8143 6403 4153 6427", "204800")
tests.add("24\n4303 5379 9287 2985 4049 1205 4815 1483 5221 2637 5765 8969 7907 7621 9629 7083 3775 2983 4211 3195 4011 7111 6103 8103", "153600")
tests.add("24\n4233 6553 2973 1497 1187 2401 6259 5889 2731 5953 5245 2423 4199 4663 8127 3875 7841 5855 3177 7771 9961 4643 5917 6811", "274432")
