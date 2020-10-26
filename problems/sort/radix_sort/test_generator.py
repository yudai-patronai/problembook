#!/usr/bin/python3
import os
from lib import random
from lib.testgen import TestSet


def radixSort(arrayToSort):
    answer = ''
    n = len(arrayToSort)
    maxx = max(arrayToSort)
    p = 0
    while maxx > 0:
        p+=1
        maxx//=10
    for i in range(p):
        zero = []
        one =[]
        for j in range(n):
            if (arrayToSort[j] % 10**(i+1)) // (10**i) ==1:
                one.append(arrayToSort[j])
            else:
                zero.append(arrayToSort[j])
        arrayToSort = zero + one
        answer += ' '.join(list(map(str, arrayToSort)))
        answer += '\n'
    return answer

NUM_TEST = 10
random.seed(10000)

tests = TestSet()

for i in range(1, NUM_TEST + 1):
    n = random.randint(1, 10)
    array = [random.randint(0, 16) for _ in range(n)]
    question = [int(bin(val)[2:]) for val in array]
    answer = radixSort(question)
    question = ' '.join(list(map(str, question)))
    tests.add(question, answer)
