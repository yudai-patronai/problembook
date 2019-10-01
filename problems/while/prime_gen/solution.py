def isprime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True

def gen_prime(n):
    iter = 1
    guess = 2

    while iter < n:
        guess += 1
        if isprime(guess):
            iter += 1
    
    return guess

n = int(input())
print(gen_prime(n))