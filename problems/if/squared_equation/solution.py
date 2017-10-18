def count_positive_roots(a, b, c):

	if a == b == c == 0:
		return -1
	
	if a == 0:
		if c * b >= 0:
			return 0
		else:
			return 1
	
	if c * a < 0:
		return 1

	if c == 0:
		if b * a >= 0:
			return 0
		else:
			return 1

	if c * a > 0:
		if b * a < 0: 
			if b**2 - 4 * a * c != 0:
				return 2
			else:
				return 1
		else:
			return 0		


if __name__ == '__main__':

	a = int(input())
	b = int(input())
	c = int(input())

	print(count_positive_roots(a, b, c))