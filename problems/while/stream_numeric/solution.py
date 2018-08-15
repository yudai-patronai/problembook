sybmol = None
Max = 0
Min = 101
count = 0
Composition = 0
triple_sum = 0
Sum = 0

while True:
    symbol = input().strip()

    if symbol == '#':
        break

    numeric = int(symbol)
    count += 1
    triple_sum += numeric
    Sum += numeric

    if numeric > Max:
        Max = numeric

    if numeric < Min:
        Min = numeric

    if count % 3 == 0:
        Composition += (triple_sum % numeric)
        triple_sum = 0

print(' '.join(map(str, [round(Sum / count, 3), Max, Min, Composition])))
