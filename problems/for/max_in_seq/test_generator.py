import os
import shutil
import random


N = 10
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
	if num == 1:
		cur_random_int = random.randint(1, 10000)
		seq = [cur_random_int for i in range(random.randint(1, 50))]
		seq.append(0)
	elif num == 2:
		seq = [1 for i in range(random.randint(1, 50))]
		seq.append(0)	
	elif num == 3:
		seq = [random.randint(1, 10000), 0]
	elif num == 4:
		seq = [random.randint(1, 100) for i in range(random.randint(1, 100))]
		seq.append(max(seq)+1)
		seq.append(0)
	else:
		cur_max_random = random.randint(100, 100000)
		seq = [random.randint(1, cur_max_random) for i in range(random.randint(10, 10000))]
		seq.append(0)
	
	with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
		f.write("\n".join(map(str, seq)))

	with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
		f.write(str(max(seq)))