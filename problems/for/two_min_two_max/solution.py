N = int(input())
line = input().split()
max1 = max2 = 0
min1 = min2 = 1000001	
for word in line:
    x = int(word)
    if x > max2:
        max2 = x
    if max2 > max1:
        max1, max2 = max2, max1
    if x < min2:
        min2 = x
    if min2 < min1:
        min1, min2 = min2, min1

print(min1 + min2, max1 + max2)
