if __name__ == "__main__":
    ans = 0
    while True:
        v, num = input().strip().split()
        v = int(v)
        if num == "A999AA":
            break
        if v <= 60:
            continue
        s = set(num[1:4])
        if len(s) == 1:
            ans += 1000
        elif len(s) == 2:
            ans += 500
        else:
            ans += 100
    print(ans)
