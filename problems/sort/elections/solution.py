n = int(input())
a = sorted(list(map(int, input().split())))
s = 0
for i in range(n // 2 + 1):
    s += a[i] // 2 + 1
print(s)