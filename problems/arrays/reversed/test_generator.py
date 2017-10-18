import os
import shutil
from lib import random


N = 6
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
	if num == 1:
		seq = [random.randint(1, 10000)]

	elif num == 2:
		seq = [random.randint(1, 10000)]*3
	
	elif num == 3:
		seq = [random.randint(1, 10000) for i in range(3)]
	
	else:
		cur_max_random = random.randint(100, 10000)
		seq = [random.randint(1, cur_max_random) for i in range(random.randint(10, 200))]
	
	with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
		f.write(str(len(seq)) + '\n')
		f.write('\n'.join(map(str,seq)))

	with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
		f.write('\n'.join(map(str,seq[::-1])))
