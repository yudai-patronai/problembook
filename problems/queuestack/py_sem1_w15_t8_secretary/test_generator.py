from solution import count
import shutil
import os
tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

a=[]
a.append('% 1 2 3 # % #\n')
a.append('1 -1 # 50 % #\n')
a.append('1 2 3 # 25 %\n')
a.append('1 2 3\n')
a.append('%#\n')
a.append('1 2 3 200 %\n')

for i in range(len(a)):
	with open(os.path.join(tests_dir, '{0:0>2}'.format(i+1)), 'w') as f:
		f.write(a[i])
	with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i+1)), 'w') as f:
		f.write(str(count(a[i])))
