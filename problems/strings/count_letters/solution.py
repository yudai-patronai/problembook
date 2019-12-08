not_letters = ' .,!?:;'

s = input()

count = len(s)
for nl in not_letters:
    count -= s.count(nl)

print(count)
