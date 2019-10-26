current_min = None
counter_min = 0

number = int(input())
while number != 0:
    if counter_min == 0 or number < current_min:
        current_min = number
        counter_min = 1
    elif number == current_min:
        counter_min += 1
    number = int(input())

print(counter_min)
