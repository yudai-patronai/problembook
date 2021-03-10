from collections import deque


jobs = list(map(int, input().split()))
hierarchy = list(map(int, input().split()))

queue = deque()
for job in jobs:
    for atomic in hierarchy:
        queue.appendleft(atomic)
        if atomic == job:
            break

for_print = []
while queue:
    for_print.append(queue.pop())

print(*for_print)
