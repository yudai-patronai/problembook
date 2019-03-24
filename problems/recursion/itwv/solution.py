def check(s, t, u):
    if t and s[0] == t[0] and check(s[1:], t[1:], u):
        return True
    if u and s[0] == u[0] and check(s[1:], t, u[1:]):
        return True
    return False


if __name__ == "__main__":
    s = input()
    t = input()
    u = input()
    n = len(s)
    m = len(t)
    k = len(u)
    for i in range(n - m - k + 1):
        if set(s[i:i + m + k]) != set(t) + set(u):
            continue
        if check(s[i:i + m + k], t, u):
            print("Yes")
            exit(0)
    print("No")
