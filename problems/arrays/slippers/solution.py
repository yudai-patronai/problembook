#!/usr/bin/env python3


def solve(N,A):
	mind = N
	for i in range(N):
		if A[i] < 0:
			for j in range(i + 1, min(N, i + mind)):
				if A[i] + A[j] == 0:
					mind = j - i
	if mind == N:
		return(0)
	else:
		return(mind) 


if __name__ == "__main__":
	print(solve(int(input()), list(map(int, input().split()))))
