n = int(input())
is_prime = []
for _ in range(n):
    is_prime.append(True)
is_prime[0] = False
for i in range(2, n+1):
    if is_prime[i-1]:
        print(i, end=' ')
        j = i + i
        while j <= n:
            is_prime[j-1] = False
            j += i
