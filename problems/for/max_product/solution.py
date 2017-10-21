n = int(input())
min1 = 10000
min2 = 10000
max1 = -10000
max2 = -10000

for _ in range(n):
    i = int(input())
    if i > max1:
        max1, max2 = i, max1
    elif i > max2:
        max2 = i
    if i < min1:
        min1, min2 = i, min1
    elif i < min2:
        min2 = i
if min1*min2 > max1*max2:
    print(min1*min2)
else:
    print(max1*max2)
