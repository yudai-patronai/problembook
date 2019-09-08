def check(s, t, u):
    if t == u == "":
        return True
    result = False
    if t and s[0] == t[0]:
        result |= check(s[1:], t[1:], u)
    if not result and u and s[0] == u[0]:
        result |= check(s[1:], t, u[1:])
    return result


if __name__ == "__main__":
    s = input()
    t = input()
    u = input()
    n = len(s)
    m = len(t)
    k = len(u)
    for i in range(n - m - k + 1):
        if set(s[i:i + m + k]) != set(t) | set(u):
            continue
        if check(s[i:i + m + k], t, u):
            print("Yes")
            exit(0)
    print("No")
