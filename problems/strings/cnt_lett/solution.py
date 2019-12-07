instring = input()
counters = [0] * (ord('Z') - ord('A') + 1)
for i in range(len(instring)):
    if instring[i] != ' ':
        counters[ord(instring[i]) - ord('A')] += 1
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if counters[ord(i) - ord('A')] > 0:
        print(i, counters[ord(i) - ord('A')])
