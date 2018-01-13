n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
s = 0
for i in a[:n//2]:
    s += i
for i in a[n//2:]:
    s -= i
print(s)
