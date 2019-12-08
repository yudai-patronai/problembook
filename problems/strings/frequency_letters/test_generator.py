from lib.testgen import TestSet

def gen_test(txt):
    res = ''
    counters = [0] * 26
    for i in range(len(txt)):
        if txt[i] != ' ':
            counters[ord(txt[i]) - ord('A')] += 1
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if counters[ord(i) - ord('A')] > 0:
            res += i + ' ' + str(counters[ord(i) - ord('A')]) + '\n'
    return res


my_list = [
    'B AAA  AAA',
    'PYTHON SHOULD RUN WELL ON ANY VODERN COMPUTER',
    'IT CAN TAKE SOME PRACTICE TO LEARN HOW TO CREATE GOOD VARIABLE NAMES',
    'EVERY PROGRAMMER MAKES MISTAKES AND MOST MAKE MISAKES EVERY DAY',
    'PROGRAMMING LANGUAGES ARE STRICT BUT THEY DISREGARD GOOD AND BAD SPELLING',
    'VARIABLES ARE OFTEN DESCRIBED AS BOXES YOU CAN STORE VALUES IN',
    'THE BEST WAY TO UNDERSTAND NEW PROGRAMMING CONCEPTS IS TO TRY USE THEM IN YOUR PROGRAMS',
    'A STRING IS A SERIES OF CHARACTERS',
    'WHITESPACE REFERS TO ANY NONPRINTING CHARACTER',
    'NUMBERS ARE USED QUITE OFTEN IN PROGRAMMING'
    ]
tests = TestSet()
for text in my_list:
    tests.add(text + '\n', gen_test(text))
