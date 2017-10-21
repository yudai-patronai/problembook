count = 0
Sum = 0

while True:
	number = int(input())

	if number == 0:
		break

	Sum += number
	count += 1

print(round(Sum/count, 2))