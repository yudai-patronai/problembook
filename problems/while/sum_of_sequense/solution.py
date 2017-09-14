#!/usr/bin/env python3


if __name__ == "__main__":
	s = 0
	a = int(input())
	while a != 0:
		s += a
		a = int(input())
	print(s)	

def solve(seq):
	return sum(seq)