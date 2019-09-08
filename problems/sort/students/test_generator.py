import os
import shutil
from lib import random
import string


def solution(seq):
    '''Получаем ответ из входных данных'''
    lst = sorted(seq, key=lambda x: sum(x), reverse=True)
    lst = [' '.join(map(str, sorted(sub_list, reverse=True))) for sub_list in lst]
    return lst


def seq_to_write(seq):
    seq_2_str = []
    for index, sub_list in enumerate(seq):
        for value in sub_list:
            seq_2_str.append(' '.join(map(str, [index, value])))
    #seq_2_str = [' '.join(map(str, [index, value])) for valuen in sub_list for index, sub_list in enumerate(seq)]
    random.shuffle(seq_2_str)
    return [str(len(seq))] + seq_2_str + ['#']


def seq_2_solutin(n_student, n=None):
    # генерим количество оценок. Оно будет в диапазоне от количеств студентов, до * количество студентов
    n_value = n or random.randint(n_student, 5 * n_student)

    #Возвращаем оценки в формате листа
    seq = [[] for _ in range(n_student)]
    for _ in range(n_value):
        seq[random.randint(0, n_student - 1)].append(random.randint(1, 10))
    return seq


N = 6
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = [[3, 10], [], [2, 3, 4]]

    elif num == 2:
        seq = [[], [], [2, 5, 1]]

    
    elif num == 3:
        seq = [[3, 10], [2, 2], [1, 1, 4]]

    elif num == 4:
        seq = seq_2_solutin(4, 10)
    
    else:
        seq = seq_2_solutin(50)

    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write('\n'.join(seq_to_write(seq)))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(' '.join(map(str, solution(seq))))
