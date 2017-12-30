def get_ans(x1, y1, x2, y2, depth=0):
    if not((0 < x1 < 9) and (0 < y1 < 9)):
        return -2
    if x1 == x2 and y1 == y2:
        return depth
    if depth == 2:
        return -1
    else:
        return max(get_ans(x1 + 1, y1 + 2, x2, y2, depth + 1),
                   get_ans(x1 + 1, y1 - 2, x2, y2, depth + 1),
                   get_ans(x1 - 1, y1 + 2, x2, y2, depth + 1),
                   get_ans(x1 - 1, y1 - 2, x2, y2, depth + 1),
                   get_ans(x1 + 2, y1 + 1, x2, y2, depth + 1),
                   get_ans(x1 + 2, y1 - 1, x2, y2, depth + 1),
                   get_ans(x1 - 2, y1 + 1, x2, y2, depth + 1),
                   get_ans(x1 - 2, y1 - 1, x2, y2, depth + 1)
                   )

x1, x2, x3, x4 = int(input()), int(input()), int(input()), int(input())
print(get_ans(x1, x2, x3, x4))
