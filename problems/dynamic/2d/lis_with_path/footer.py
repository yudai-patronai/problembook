def check(s1, sub):
    cur = 0
    for i in s1:
        if cur == len(sub):
                break
        if i == sub[cur]:
            cur += 1
    return cur == len(sub)

if __name__ == "__main__":
    s = list(map(int, input().split(' ')))
    sub = lis(s)
    for i in range(1, len(sub)):
        assert sub[i-1] < sub[i], "Your subsequence is not increasing"       
    assert check(s, sub), "Your answer is not a subsequence"
    print(len(sub))
