import os
import shutil
# from lib 
import random
import string

class aeroflot:
    def __init__(self, departure, destination, points_0, points_1, points_2):
        self.departure = departure
        self.destination = destination
        self.points = [points_0, points_1, points_2]

    # rework to magic method
    def to_line(self):
        lst = [self.departure, self.destination, self.points[0], self.points[1], self.points[2]]
        return ' '.join(list(map(str, lst)))


def solution(seq, departure, destination, day):
    sum = 0

    for element in seq:
        if element.departure == departure and element.destination == destination:
            sum += len(list(filter(lambda x: x >= day, element.points)))
    return sum
                


def generate_seq(n, max_):
    return [aeroflot(random.randint(1, max_), random.randint(1, max_), 
                     random.randint(1, 30), random.randint(1, 30), 
                     random.randint(1, 30)
                     ) for _ in range(n)]

N = 6
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = [aeroflot(1, 2, 5, 8, 10), aeroflot(2, 5, 10, 20, 30)]
        departure = 1
        destination = 2
        day = 7

    elif num == 2:
        seq = [aeroflot(1, 2, 5, 8, 10)]
        departure = 1
        destination = 2
        day = 11


    
    elif num == 3:
        seq = [aeroflot(1, 2, 5, 8, 10), aeroflot(1, 2, 13, 12, 8)]
        departure = 1
        destination = 2
        day = 8
    
    else:
        seq = generate_seq(100, 5)
        departure = random.choice([x.departure for x in seq])
        destination = random.choice([x.destination for x in seq])
        day = random.randint(10, 20)


    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write('{}\n'.format(len(seq)))
        f.write('\n'.join([x.to_line() for x in seq]))
        f.write('\n{} {} {}\n'.format(departure, destination, day))


    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(str(solution(seq, departure, destination, day)))
