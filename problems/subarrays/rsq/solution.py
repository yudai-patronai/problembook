if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    ps = [0]
    for i in range(n):
        ps.append(a[i] + ps[-1])
    k = int(input())
    ans = []
    for _ in range(k):
        x, y = map(int, input().split())
        ans.append(str(ps[y+1] - ps[x]))
    print(" ".join(ans))
