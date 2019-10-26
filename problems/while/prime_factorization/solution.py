def prime_factorization(n):
    factor = 2
    while n * n > factor + 1:
        if n % factor == 0:
            n //= factor
            print(factor)
        else:
            factor += 1

n = int(input())
prime_factorization(n)