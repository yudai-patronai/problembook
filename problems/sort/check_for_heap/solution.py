n = int(input())
a = [int(input()) for _ in range(n)]
for i in reversed(range(1, n)):
    if a[(i-1)//2] < a[i]:
        print("NO")
        exit(0)
print("YES")
