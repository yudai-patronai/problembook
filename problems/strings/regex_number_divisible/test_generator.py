import string
from lib.testgen import TestSet
from lib import random
import math
import queue

tests = TestSet()

tests.add("0", "YES")
tests.add("1", "YES")
tests.add("2", "YES")

tests.add("3 7 63 70 114 246 231 201 119", "Token: 734dafc3371d524b\nYES")
