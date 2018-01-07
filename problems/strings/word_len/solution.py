Max = 0
Min = 1001

for word in input().split(' '):
    if len(word) > Max:
        Max = len(word)
    if len(word) < Min:
        Min = len(word)

print(Min, Max)
