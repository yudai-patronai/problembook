current_max = None
counter_max = 0

number = int(input())
while number != 0:
    if counter_max == 0 or number > current_max:
        current_max = number
        counter_max = 1
    elif number == current_max:
        counter_max += 1
    number = int(input())

print(counter_max)
