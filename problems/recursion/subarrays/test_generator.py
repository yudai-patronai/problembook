import os
import shutil
import subprocess
import sys


def printSubArrays(arr, start, end, f):
	#stop at the end	
	if end == len(arr):
		return
	# Increment the end point and start from 0 
	elif start > end:
		return printSubArrays(arr, 0, end + 1,f) 
	# Print the subarray and increment start
	else:
		print(arr[start], type(arr[start]))
		f.write(' '.join(arr[start:end + 1])+'\n')
		return printSubArrays(arr, start + 1, end,f)


#NUM_TEST = 50

#random.seed(42)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

# number of elements grows up to 43 (not to exceed recursion limit)
l=[5,10,20,42]
for i in range(1,len(l)+1):
	array=list(map(str,range(l[i-1])))
	# store it as task input
	with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as fin:
		fin.write(' '.join(val for val in array) + '\n')

	# sort and save it as expected output
	with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as fout:
		printSubArrays(array, 0, 0, fout)

#one element
with open(os.path.join(tests_dir, '05'), 'w') as fin:
	fin.write('0')
with open(os.path.join(tests_dir, '05.a'), 'w') as fin:
	fin.write('0')
#empty test
# with open(os.path.join(tests_dir, '06'), 'w') as fin:
# 	fin.write('')
# with open(os.path.join(tests_dir, '06.a'), 'w') as fin:
# 	fin.write('')
