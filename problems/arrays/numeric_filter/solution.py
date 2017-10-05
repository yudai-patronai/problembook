n = int(input())
seq = [0]*n
for i in range(n):
    seq[i] = int(input())
x = int(input())
ans = []
for i in range(n):
    if seq[i] % x == 0:
        ans.append(str(i))
if len(ans):
    print(' '.join(ans))
else:
    print(-1)
