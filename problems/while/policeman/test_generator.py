from lib import random
import re
import os
import shutil

number_pattern = re.compile(r'(?P<speed>\d+)\s+[A-Z](?P<number>\d{3})[A-Z]{2}')
regnumber_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def determine_tax(regnum):
    unique_digits = len(set(regnum[1:4]))
    if unique_digits == 3:
        return 100
    if unique_digits == 2:
        return 500
    if unique_digits == 1:
        return 1000


def calculate_salary(lines):
    summa = 0
    for line in lines:
        speed, regnum = line.split()
        speed = int(speed)
        if regnum == "A999AA":
            break
        if speed > 60:
            summa += determine_tax(regnum)
    return summa


N = 15
random.seed(10000)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)


def generate_entry():
    speed = random.randint(10, 120)
    number = random.randint(100, 1000)
    a = random.choice(regnumber_letters)
    b = random.choice(regnumber_letters)
    c = random.choice(regnumber_letters)
    return str(speed) + ' ' + str(a) + str(number) + str(b) + str(c)


def generate_test_input():
    test_input_len = random.randint(3, 100)
    result = []
    for i in range(test_input_len):
        result.append(generate_entry())
    chief_speed = random.randint(10, 120)
    result.append(str(chief_speed) + " A999AA")
    return result


for i in range(1, N + 1):

    test_input = generate_test_input()

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        for x in test_input:
            f.write(x + '\n')

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        salary = calculate_salary(test_input)
        f.write(str(salary))

