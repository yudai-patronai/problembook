def factorial_trailing_zeros(n):
    pow_of_5 = 5
    zeros = 0
    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5
    return zeros


n = int(input())
print(factorial_trailing_zeros(n))
