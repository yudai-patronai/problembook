n = int(input())
events = []
for i in range(n):
    events.append(tuple([int(input()) for _ in range(3)]))
m = int(input())
for i in range(m):
    panel = int(input())
    ans = 0
    for j in reversed(range(n)):
        if events[j][0] <= panel <= events[j][1]:
            ans = events[j][2]
            break
    print(ans, end=' ')
