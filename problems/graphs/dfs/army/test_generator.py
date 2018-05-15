import os
import shutil
from lib import random


N = 8
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)


def generate_array(n, m, answer):
    element = list(range(1, n+1))
    element = random.sample(element, n)
    random.shuffle(element)
    seq = []
    if answer == 'Yes':
        for _ in range(m):
            left = random.randint(0, n-2)
            right = random.randint(left+1, n-1)
            seq.append([element[left], element[right]])

    if answer == 'No':
        negative = random.randint(1, int(m/2))
        for _ in range(m-negative):
            left = random.randint(0, n-2)
            right = random.randint(left+1, n-1)
            seq.append([element[left], element[right]])

        for _ in range(negative):
            left = random.randint(0, n-2)
            right = random.randint(left+1, n-1)
            seq.append([element[right], element[left]])
    return seq



for num in range(1, N + 1):
    if num == 1:
        n = 5
        m = 6
        answer = 'No'
        seq = [[4, 5], [1, 2], [2, 3], [3, 4], [1, 4], [4, 1]]
        
    elif num == 2:
        n = 5
        m = 5
        answer = 'Yes'
        seq = [[4, 5], [1, 2], [2, 3], [3, 4], [1, 4]]            

    elif num == 3:
        n = 5
        m = 7
        answer = 'Yes'
        seq = generate_array(n, m, answer)
    
    else:
        n = random.randint(7, 30)
        m = random.randint(1, int(n * n / 2))
        answer = random.choice(['Yes', 'No'])
        seq = generate_array(n, m, answer)
    seq = [' '.join(map(str, sub_list)) for sub_list in seq]    
    
    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(' '.join([str(n), str(m)]))
        f.write('\n')
        print(seq)
        f.write('\n'.join(seq))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(answer)