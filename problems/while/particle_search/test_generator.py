from lib.testgen import TestSet
from lib.random import randint, sample
from string import ascii_letters


MAX_NAME_LEN = 20

MAX_TIME = 24 * 3600000 - 1
MAX_INTERVAL = MAX_TIME // 100000
MAX_GROUP_SIZE = 5000
MAX_LOGS_COUNT = 50000
USUAL_RANDOM_SIZE = 40000


class Times:
    def __init__(self):
        self.__time = 0
        self.__logs = []

    def __add_time(self):
        self.__logs.append(self.__time)
        return len(self.__logs) - 1

    def add(self, min_start_interval=1):
        self.__time += randint(min_start_interval, MAX_INTERVAL)
        return self.__add_time()

    def add_many(self, min_start_interval=1):
        start_count = randint(1, MAX_GROUP_SIZE)
        start = self.add(min_start_interval)
        for _ in range(start_count - 1):
            self.__add_time()
        return start, start + start_count

    def get_logs(self):
        return list(self.__logs)

    def get_log(self, i):
        return self.__logs[i]


def time_to_str(time):
    return '{h:02}:{m:02}:{s:02}.{ms:003}'.format(
        h= time // 3600000,
        m= time % 3600000 // 60000,
        s= time % 60000 // 1000,
        ms= time % 1000)


def gen_name(length):
    return ''.join(sample(ascii_letters, length))


# Нужны следующие группы тестов:
#1 ключ совпадает с первым временем, может быть целая группа идентичного времени
#2 ключ совпадает с последним временем, может быть целая группа идентичного времени
#3 ключ совпадает с каким-то временем из середины, может быть целая группа идентичного времени
#4 ключ не совпадает, находится между двух групп
#5(не используется) ключ не совпадает, находится между двух одиночных
#6 ключ меньше меньшего времени
#7 ключ больше большего времени
def gen_test(test_type):
    times = Times()

    if test_type == 1 or test_type == 6:
        res = list(range(*times.add_many()))
        times.add()
        for _ in range(USUAL_RANDOM_SIZE - 1):
            times.add(min_start_interval=0)
        logs = times.get_logs()
        key = logs[0] if test_type == 1 else randint(0, logs[0] - 1)

    elif test_type == 2 or test_type == 7:
        for _ in range(USUAL_RANDOM_SIZE):
            times.add(min_start_interval=0)
        res = list(range(*times.add_many()))
        logs = times.get_logs()
        key = logs[-1] if test_type == 2 else randint(logs[-1] + 1, MAX_TIME)

    elif test_type == 3:
        for _ in range(USUAL_RANDOM_SIZE // 2):
            times.add(min_start_interval=0)
        res = list(range(*times.add_many()))
        times.add()
        for _ in range(USUAL_RANDOM_SIZE // 2 - 1):
            times.add(min_start_interval=0)
        logs = times.get_logs()
        key = logs[res[0]]

    elif test_type == 4:
        for _ in range(USUAL_RANDOM_SIZE // 2):
            times.add(min_start_interval=0)
        l = times.add_many()
        r = times.add_many(min_start_interval=2)
        times.add()
        for _ in range(USUAL_RANDOM_SIZE // 2 - 1):
            times.add(min_start_interval=0)
        logs = times.get_logs()
        res = list(range(*l)) + list(range(*r))
        key = randint(logs[l[1]], logs[r[0] - 1])

    return {
        'logs': logs,  # list of ints - time in milliseconds
        'time': key,  # input time -> int
        'res': res  # list of ints - positions of needed times
        }


def question(test_dict, names):
    logs = '\n'.join('{} {}'.format(time_to_str(time), name) \
        for time, name in zip(test_dict['logs'], names))
    time = time_to_str(test_dict['time'])
    return '{}\n#\n{}'.format(logs, time)


def answer(test_dict, names):
    return '{}\n'.format(' '.join(sorted(names[i] for i in test_dict['res'])))


tests = TestSet()
def add_test(test_dict):
    names = [gen_name(randint(MAX_NAME_LEN)) for _ in range(len(test_dict['logs']))]
    tests.add(question(test_dict, names), answer(test_dict, names))


for test_type in [1, 2, 3, 4, 6, 7]:
    for _ in range(2):
        add_test(gen_test(test_type))
