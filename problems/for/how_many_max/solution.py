number = -1
current_max = -1
dct = dict()

while number != 0:
    number = int(input())

    dct[number] = dct.get(number, 0) + 1

    if number > current_max:
        current_max = number

print(dct[current_max])
