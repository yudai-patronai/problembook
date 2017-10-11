dct = {}

while True:
	number = int(input())
	if number == 0:
		break
	dct[number] = dct.get(number, 0) + 1

print(max(dct, key=dct.get))
