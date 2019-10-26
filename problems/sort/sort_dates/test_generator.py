from lib.testgen import TestSet
from lib.random import randint, shuffle

MONTHES = [
    ('January', 31),
    ('February', 28),
    ('March', 31),
    ('April', 30),
    ('May', 31),
    ('June', 30),
    ('July', 31),
    ('August', 31),
    ('September', 30),
    ('October', 31),
    ('November', 30),
    ('December', 31)
]


def join_dates(arr):  # util for print
    s = ''
    for a in arr:
        s += '{} {} {} {}:{:02d}\n'.format(*a)

    return s


def sort_key(date_entry):  #  for sort function
    month_index = -1
    for i,m in enumerate(MONTHES):
        if m[0] == date_entry[1]:
            month_index = i
            break

    return date_entry[2], month_index, date_entry[0], date_entry[3], date_entry[4]


def random_dates(size):
    dates = []
    for _ in range(size):
        month, max_day = MONTHES[randint(0, len(MONTHES)-1)]
        day = randint(1, max_day)
        year = randint(2018, 2019)
        hours = randint(0, 23)
        mins = randint(0, 59)
        date = [day, month, year, hours, mins]
        dates.append(date)

    return dates


def question(dates):
    return '{}\n'.format(len(dates)) + join_dates(dates)


def answer(question_dates):
    sorted_dates = list(sorted(question_dates, key=sort_key))
    return join_dates(sorted_dates)


tests = TestSet()

tests.add(
    '3\n' + join_dates([
        [20, 'December', 2019, 16, 0],
        [20, 'January', 2015, 16, 0], 
        [20, 'November', 2019, 16, 0],
    ]),
    join_dates([
        [20, 'January', 2015, 16, 0], 
        [20, 'November', 2019, 16, 0],
        [20, 'December', 2019, 16, 0],
    ])
)

manual_test = [
    [20, 'January', 2019, 19, 30], # min
    [20, 'January', 2019, 19, 40],
    [20, 'January', 2019, 19, 10],
    [20, 'January', 2019, 19, 0], # h
    [20, 'January', 2019, 12, 0],
    [20, 'January', 2019, 16, 0], 
    [20, 'January', 2019, 16, 0], # year
    [20, 'January', 2010, 16, 0], 
    [20, 'January', 2015, 16, 0], 
    [20, 'December', 2019, 16, 0], # month
    [20, 'November', 2019, 16, 0],
    [20, 'October', 2019, 16, 0], 
    [20, 'September', 2019, 16, 0], 
    [20, 'July', 2019, 16, 0], 
    [20, 'June', 2019, 16, 0], 
    [20, 'August', 2019, 16, 0], 
    [20, 'May', 2019, 16, 0], 
    [20, 'March', 2019, 16, 0], 
    [20, 'February', 2019, 16, 0], 
    [20, 'January', 2019, 16, 0], 
    [20, 'April', 2019, 16, 0],  
]

tests.add(
    question(manual_test),
    answer(manual_test)
)

dates = random_dates(10)
tests.add(
    question(dates),
    answer(dates)
)


dates = random_dates(200)
tests.add(
    question(dates),
    answer(dates)
)