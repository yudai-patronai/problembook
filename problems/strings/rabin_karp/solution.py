MODULE = 1 << 64


def poly_hash(s):
    h = [0]
    p = [1]
    base = 257
    for c in s:
        h.append(((h[-1] * base) % MODULE + ord(c)) % MODULE)
        p.append((p[-1] * base) % MODULE)
    return (h, p)


if __name__ == "__main__":
    s = input()
    t = input()
    s_hash, _ = poly_hash(s)
    s_hash = s_hash[-1]
    h, p = poly_hash(t)
    flag = False
    for l in range(len(t) - len(s) + 1):
        r = l + len(s)
        if s_hash == (h[r] - (h[l] * p[r - l]) % MODULE) % MODULE:
            print(l, end=' ')
            flag = True
    if not flag:
        print(-1)
    else:
        print()
