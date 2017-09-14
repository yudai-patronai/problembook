import os
import shutil
import random


N = 50
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
	seq = [random.randint(1, 10000) for i in range(random.randint(1, 10000))]
	seq.append(0)

	with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
		f.write("\n".join(map(str, seq)))

	with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
		f.write(str(max(seq)))