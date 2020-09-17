counts = [0, 0, 0, 0]
n = int(input())
for i in range(n):
    x, y = [int(e) for e in input().split()]
    if x * y != 0:
        if x > 0 and y > 0:
            counts[0] += 1
        elif x < 0 and y > 0:
            counts[1] += 1
        elif x < 0 and y < 0:
            counts[2] += 1
        else:
            counts[3] += 1
j, aj = max(enumerate(counts), key=lambda e: e[1])
print(j+1, aj)
