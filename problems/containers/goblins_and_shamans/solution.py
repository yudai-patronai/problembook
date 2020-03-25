from collections import deque
from math import ceil

if __name__ == "__main__":
    n = int(input())
    queue = deque()
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == "+":
            queue.append(cmd[1])
        elif cmd[0] == "*":
            pos = ceil(len(queue) / 2)
            queue.insert(pos, cmd[1])
        else:
            print(queue.popleft())
