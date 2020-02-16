M = (1 << 61) - 1
B = 257


def poly_hash(s):
    h = [0]
    p = 1
    for c in s:
        h.append(((h[-1] * B) % M + ord(c)) % M)
        p.append((p * B) % M)
    return (h, p)


if __name__ == "__main__":
    s = input()
    t = input()
    s_hash, _ = poly_hash(s)
    s_hash = s_hash[-1]
    h, p = poly_hash(t)
    pos = []
    for l in range(len(t) - len(s) + 1):
        r = l + len(s)
        if s_hash == (h[r] - (h[l] * p) % M) % M:
            pos.append(str(l))
    if not pos:
        print(-1)
    else:
        print(" ".join(pos))
