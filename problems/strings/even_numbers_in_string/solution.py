s = input()

count = 0
for el in s:
    if el.isdigit() and int(el) % 2 == 0:
        count += 1
print(count)
