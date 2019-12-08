from lib.testgen import TestSet
from lib.random import randint



tests = TestSet()

q1 = '6\ndesktop Netscape Navigator\ndesktop Opera\ndesktop Google Chrome\n' +
    'mobile Opera\ndesktop Google Chrome\nmobile Google Chrome\n'
a1 = 'desktop browsers raiting\n1 Google Chrome\n2 - 3 Netscape Navigator\n' +
    '2 - 3 Opera\nmobile browsers raiting\n1 - 2 Opera\n1 - 2 Google Chrome\n'
tests.add(q1, a1)
