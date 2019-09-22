line = input()
max_number = -1

number = 0
for symbol in line:
    if '0' <= symbol <= '9':
        digit = int(symbol)
        number = number * 10 + digit  # собираем число по схеме Горнера
    else:
        if number > max_number:
            max_number = number
        number = 0
print(max_number)
