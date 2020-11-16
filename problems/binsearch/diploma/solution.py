def bin_search(n, x, greater_or_equal):
    l, r = 0, n-1
    while l < r:
        m = (l + r) // 2
        if greater_or_equal(m, x):
            l, r = l, m
        else:
            l, r = m+1, r
    return l


def is_correct_square_side(side, whn):
    return (side // whn[0]) * (side // whn[1]) >= whn[2]


def calc_min_square_side(w, h, n):
    if n == 0:
        return 0
    if w == 0:
        return h
    if h == 0:
        return w
    max_side = max(w, h) * n
    return bin_search(max_side + 1, (w, h, n), is_correct_square_side)


w, h, n = map(int, input().split())
print(calc_min_square_side(w, h, n))
