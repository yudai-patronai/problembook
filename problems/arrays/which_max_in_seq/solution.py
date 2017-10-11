dct = {}

N = int(input())
for _ in range(N):
    number = int(input())
    dct[number] = dct.get(number, 0) + 1

print(max(dct, key=dct.get))
