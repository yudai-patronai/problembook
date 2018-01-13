mx = [0] * 6
cur = -1
while True:
    elem = int(input())
    cur = (cur + 1) % 6
    if elem == 0:
        break
    mx[cur] = max(mx[cur - 1], elem)
print(mx[cur])
