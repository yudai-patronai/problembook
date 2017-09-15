#!/usr/bin/env python3

def solve(s):
	count=0
#	nums=map(int(),s.split())
	nums=[int(i) for i in s.split()]
	for x in nums:
		if not x:
			break
		elif not x%2:
			count+=1
	print(count)
	return count

if __name__=="__main__":
	solve(input())
