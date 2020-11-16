ef binary_search(seq, x):
    answer = -1
    l = 0
    r = len(seq) - 1
    while (l <= r):
        m = (l + r) // 2
        if (seq[m] == x):
            answer = m + 1
            break
        elif (seq[m] > x):
            r = m - 1
        else:
            l = m + 1
    return answer


