n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
i, j = 0, 0
c = None
while i < len(a) and j < len(b):
    while i < len(a) and a[i] == c:
        i += 1
    while j < len(b) and b[j] == c:
        j += 1
    if i >= len(a) or j >= len(b):
        break
    if a[i] != b[j]:
        print('No')
        exit(0)
    c = a[i]
if i < len(a) or j < len(b):
    print('No')
else:
    print('Yes')
