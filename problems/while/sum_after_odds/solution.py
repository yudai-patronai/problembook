def sum_after_odds():
    s = 0

    prev_elem = int(input())
    if prev_elem != 0:
        elem = int(input())
        if elem == 0:
            return -1
    else:
        return -1

    while elem != 0:
        if prev_elem % 2 != 0:
            s += elem
        prev_elem = elem
        elem = int(input())

    s = -1 if s == 0 else s

    return s

result = sum_after_odds()
print(result)