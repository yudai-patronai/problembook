N = int(input())
arr = [int(input()) for _ in range(N)]
M = int(input())

base = arr[M]
count = 0
for i in arr:
    if i > base:
        count += 1
print(count)
