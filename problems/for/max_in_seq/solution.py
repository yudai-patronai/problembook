number = -1
current_max = -1

while number != 0:
	number = int(input())
	if number > current_max:
		current_max = number

print(current_max)

