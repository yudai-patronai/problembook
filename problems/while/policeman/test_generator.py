from lib import random
import re
import os
import shutil

number_pattern = re.compile(r'(?P<speed>\d+)\s+[а-я](?P<number>\d{3})[а-я]{2}')
russian_letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')


def read_taxed_numbers(lines):
    taxed_numbers = []
    for line in lines:
        number = read_entry(line)
        if number != None:
            taxed_numbers.append(number)
    return taxed_numbers


def read_entry(line):
    groups = number_pattern.fullmatch(line)
    if groups == None:
        return None
    speed = int(groups.group("speed"))
    if (speed <= 60):
        return None
    return groups.group("number")


def determine_tax(number):
    unique_digits = len(set(number))
    if unique_digits == 3:
        return 100
    if unique_digits == 2:
        return 500
    if unique_digits == 1:
        return 1000


def calculate_salary(numbers):
    sum = 0
    for number in numbers:
        sum += determine_tax(number)
    return sum


N = 50
random.seed(10000)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)


def generate_entry():
    speed = random.randint(10, 100)
    number = random.randint(100, 1000)
    a = random.choice(russian_letters)
    b = random.choice(russian_letters)
    c = random.choice(russian_letters)
    return str(speed) + ' ' + str(a) + str(number) + str(b) + str(c)


def generate_list():
    x = random.randint(10, 100)
    result = []
    for i in range(x):
        result.append(generate_entry())
    return result


for i in range(1, N + 1):

    test_input = generate_list()

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        for x in test_input:
            f.write(x + '\n')

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        values = read_taxed_numbers(test_input)
        salary = calculate_salary(values)
        f.write(str(salary))
