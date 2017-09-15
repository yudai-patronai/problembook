#!/usr/bin/python3

import os
import random
import solution

random.seed(10000)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
os.makedirs(tests_dir)

with open(os.path.join(tests_dir, '01'),'w') as f:
	f.write('0')

"""
with open(os.path.join(tests_dir, '01.a'),'w') as file:
	file.write('0')
"""

with open(os.path.join(tests_dir, '02'),'w') as f:
	f.write('0 2 2')

"""
with open(os.path.join(tests_dir, '02.a'),'w') as file:
	file.write('0')
"""

for i in range(3,7):
	row=[random.randint(-50,50) for j in range(5*i)]
	with open(os.path.join(tests_dir, '{0:0>2}'.format(i)),'w') as f:
		for k in row:	
			f.write(str(k)+' ')
		f.write('0')

for i in range(1,7):
	with open(os.path.join(tests_dir, '{0:0>2}'.format(i)),'r') as ques:
		ans=str(solution.solve(ques.read()))

	with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)),'w') as out:
		out.write(ans)
	
