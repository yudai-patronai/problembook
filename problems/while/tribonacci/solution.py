def get_trib_number(n):
    if n == 0:
        return 2
    num = 2
    t0 = t1 = 0
    t2 = 1
    cur = 0
    while cur <= n:
        cur = t0 + t1 + t2
        t0, t1, t2 = t1, t2, cur
        num += 1
    return num


if __name__ == "__main__":
    n = int(input())
    print(get_trib_number(n))
