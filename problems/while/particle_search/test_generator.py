from lib.testgen import TestSet
from lib.random import randint


MAX_TIME = 24 * 3600000 - 1
MAX_INTERVAL = MAX_TIME // 100000
MAX_GROUP_SIZE = 100
MAX_LOGS_COUNT = 50000
USUAL_RANDOM_SIZE = 100


class Times:
    def __init__(self):
        self.__time = 0
        self.__logs = []

    def __add_time(self):
        self.__logs.append(self.__time)
        return len(self.__logs) - 1

    def add(self, min_interval=1):
        self.__time += randint(min_interval, MAX_INTERVAL)
        return self.__add_time()

    def add_many(self, min_interval=1):
        start_count = randint(1, MAX_GROUP_SIZE)
        start = self.add(min_interval)
        for _ in range(start_count - 1):
            self.__add_time()
        return start, start + start_count

    def get_logs(self):
        return list(self.__logs)

    def get_log(self, i):
        return self.__logs[i]


def entry_to_str(time, t):
    return '{h:02}:{m:02}:{s:02}.{ms:003} {t}'.format(
        h= time // 3600000,
        m= time % 3600000 // 60000,
        s= time % 60000 // 1000,
        ms= time % 1000,
        t= t)


# Нужны следующие группы тестов:
#1 ключ совпадает с первым временем, может быть целая группа идентичного времени
#2 ключ совпадает с последним временем, может быть целая группа идентичного времени
#3 ключ совпадает с каким-то временем из середины, может быть целая группа идентичного времени
#4 ключ не совпадает, находится между двух групп
#5 ключ не совпадает, находится между двух одиночных
#6 ключ меньше меньшего времени
#7 ключ больше большего времени


def gen_test(test_type):
    times = Times()

    if test_type == 1 or test_type == 6:
        res = list(range(*times.add_many()))
        times.add()
        for _ in range(2 * randint(USUAL_RANDOM_SIZE) - 1):
            times.add(min_interval=0)
        logs = times.get_logs()
        key = logs[0] if test_type == 1 else randint(0, logs[0] - 1)

    elif test_type == 2 or test_type == 7:
        for _ in range(2 * randint(USUAL_RANDOM_SIZE)):
            times.add(min_interval=0)
        res = list(range(*times.add_many()))
        logs = times.get_logs()
        key = logs[-1] if test_type == 2 else randint(logs[-1] + 1, MAX_TIME)

    elif test_type == 3:
        for _ in range(randint(USUAL_RANDOM_SIZE)):
            times.add(min_interval=0)
        res = list(range(*times.add_many()))
        times.add()
        for _ in range(randint(USUAL_RANDOM_SIZE) - 1):
            times.add(min_interval=0)

    elif test_type == 4:
        pass

    return {
        'logs': logs,  # list of ints - time in milliseconds
        'key': key,  # input time -> int
        'res': res  # list of ints - positions of needed times
        }


tests = TestSet()