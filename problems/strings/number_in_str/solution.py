number = [str(i) for i in range(10)]
current_numer = ''
multiple = 1
is_number = False


for symbol in input().strip() + '#':
    if symbol in number:
        is_number = True
        current_numer += symbol
        continue

    if is_number:
        multiple *= int(current_numer)
        is_number = False
        current_numer = ''

print(multiple)
