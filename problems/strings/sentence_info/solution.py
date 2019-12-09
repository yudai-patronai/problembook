list = input().split()
i = 1
cnt = 0
for wrd in list:
    cnt += 1
    if wrd[-1] == ',':
        continue
    if wrd[-1].isalnum():
        continue
    print(i, cnt);
    i += 1
    cnt = 0
