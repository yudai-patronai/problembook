def is_add_35(n):
    if n < 1:
        return False
    elif n == 1:
        return True
    else:
        return is_add_35(n - 3) or (n - 1) % 5 == 0
