number = int(input())
decomposition = ''
power = 0

while number > 0:
    digit = number % 10

    term = str(digit) + '*10^' + str(power)

    if power == 0:
        decomposition = term
    else:  # power = 1, 2, ...
        decomposition = term + ' + ' + decomposition

    number //= 10
    power += 1

print(decomposition)
