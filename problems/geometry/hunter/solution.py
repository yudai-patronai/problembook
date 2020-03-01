def tg(x, y):
    if x == 0:
        if y > 0:
            return float("inf"), y > 0
        return - float("inf"),  y > 0
    if y == 0:
        if x > 0:
            return 1 / 1001, x > 0
        return -1 / 1001, x > 0
    return y / x, x > 0


targets = dict()
n = int(input())
for i in range(n):
    x, y = tuple(map(int, input().split()))
    tang = tg(x, y)
    if tang in targets:
        targets[tang] += 1
    else:
        targets.update({tang: 1})
maxx = 0
for tan in targets:
    if targets[tan] > maxx:
        maxx = targets[tan]
print(maxx)
