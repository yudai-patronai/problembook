from solution import count
import shutil
import os
tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

a=[]
a.append('% 1 2 3 # % #')
a.append('1 -1 # 50 % #')
a.append('1 2 3 # 25 % #')
a.append('1 2 3')
a.append('%#')
a.append('1 2 3 200 %')

for i in range(len(a)):
	with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
		f.write(a[i])
	with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
		f.write(str(count(a[i])))
