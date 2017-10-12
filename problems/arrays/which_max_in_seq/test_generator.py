import os
import shutil
from lib import random
from collections import Counter

def which_max(seq):
	dct = Counter(seq)
	return(max(dct, key=dct.get))

def make_seq(max_el, uniq_el):
	res = random.sample(range(1, max_el), uniq_el)
	random_sequence = random.sample(range(0, 99), len(res))
	seq = [j for subset in [[random_sequence[j]]*i for j, i in enumerate(res)] for j in subset]
	random.shuffle(seq)
	return([len(seq)] + seq)

N = 5
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
	if num == 1:
		seq = [1, random.randint(0, 99)]

	elif num == 2:
		seq = [3]+[random.randint(0, 99)]*3
	
	elif num == 3:
		seq = make_seq(4, 3)
	
	else:
		seq = make_seq(40, 20)

	with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
		f.write(str(which_max(seq[1:])))

	with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
		f.write('\n'.join(map(str,seq)))

