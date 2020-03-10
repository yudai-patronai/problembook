from solution import play
import shutil
import os
tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

a=[]
a.append('a1 a2 a3 a4')
a.append('a0 c1 b2 c5 d8 b4 c4')
a.append('c2')
a.append('a3 b3 c3 d3 a1')
a.append('b8 c9 a0 a1 b2 c3 c4 d5')

for i in range(len(a)):
	with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
		f.write(a[i])
	with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
		f.write(str(play(a[i])))