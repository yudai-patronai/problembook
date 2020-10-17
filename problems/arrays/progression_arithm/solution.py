a, d, N = map(int, input().split())

A = [0] * N
A[0] = a

for i in range(1, len(A)):
    A[i] = A[i-1] + (a + d * i)

print(*A)
