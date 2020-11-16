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
    if side == 0:
        return whn[2] == 0
    n1 = float('inf') if whn[0] == 0 else side // whn[0]
    n2 = float('inf') if whn[1] == 0 else side // whn[1]
    return n1 * n2 >= whn[2]

def calc_min_square_side(w, h, n):
    max_side = max(w, h) * n
    return bin_search(max_side + 1, (w, h, n), is_correct_square_side)


w, h, n = map(int, input().split())
print(calc_min_square_side(w, h, n))
