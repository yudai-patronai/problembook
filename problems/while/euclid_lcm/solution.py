def lcm(a, b):
    m = a * b

    if a > b:
        a, b = b, a

    while a != 0:  # euclid, b is gcd after cycle
        a, b = b % a, a

    return m // b
