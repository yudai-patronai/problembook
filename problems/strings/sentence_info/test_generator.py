from lib.testgen import TestSet

tests = TestSet()

tests.add('I like reading. But first, I want to sleep.\n', '1 3\n2 6\n')
tests.add('Every day in elementary school in America begins at 9.20 a.m. Children have classes till 3.15 p.m. At 12 o’clock children have lunch. Many boys and girls bring their lunch from home. But some of them go for lunch to a school cafeteria.\n',\
    '1 11\n2 6\n3 6\n4 9\n5 11\n')
tests.add('Hello, how are you? I am OK. And you are beautiful! Bye...\n', '1 4\n2 3\n3 4\n4 1\n')
