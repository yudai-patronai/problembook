from collections import defaultdict


if __name__ == "__main__":
	pc = PrefixClass()
	dct = defaultdict(pc)
	elems = list(map(int, input().split()))
	PREFIX = elems.pop(0)
	result_list = [dct[elem] for elem in elems]
	print(''.join(result_list))
