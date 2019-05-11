
def check(s1, s2, sub):
    cur = 0
    for i in s1:
        if cur == len(sub):
            break
        if i == sub[cur]:
            cur += 1
    if cur < len(sub):
        return False
    cur = 0
    for i in s2:
        if cur == len(sub):
            break
        if i == sub[cur]:
            cur += 1
    return cur == len(sub)


if __name__ == "__main__":
    s1 = list(map(int, input().split(' ')))
    s2 = list(map(int, input().split(' ')))
    sub = lcs(s1, s2)
    assert check(s1, s2, sub), "Your answer is not a subsequence"
    print(len(sub))
