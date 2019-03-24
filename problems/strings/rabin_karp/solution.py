def poly_hash(s):
    h = [0]
    p = [1]
    base = 257
    for c in s:
        h.append(h[-1] * base + ord(c))
        p.append(p[-1] * base)
    return (h, p)


if __name__ == "__main__":
    s = input()
    t = input()
    s_hash, _ = poly_hash(s)
    s_hash = s_hash[-1]
    h, p = poly_hash(t)
    for l in range(len(t) - len(s) + 1):
        r = l + len(s)
        if s_hash == h[r] - h[l] * p[r - l]:
            print(l, end=' ')
    print()
