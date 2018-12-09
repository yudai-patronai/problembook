#!/usr/bin/env python3
from lib.testgen import TestSet
from lib.random import randint

MAX_RAND_TESTS = 20

tests = TestSet()

for _ in range(MAX_RAND_TESTS):
    tests.add("1","CORRECT")
