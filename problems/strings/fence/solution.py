s = input()

s_new = []
count = 0
for el in s:
    if el != ' ':
        if count % 2 == 0:
            s_new.append(el.upper())
        else:
            s_new.append(el.lower())
        count += 1
    else:
        s_new.append(' ')
print(''.join(s_new))