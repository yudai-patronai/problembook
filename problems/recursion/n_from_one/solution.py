def is_add_35(n):
    if n < 1:
        return False
    else:
        return n % 3 == 1 or is_add_35(n - 5)
