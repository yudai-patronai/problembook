n = int(input())
res = []
for _ in range(n):
    m = int(input())
    a = [input().split() for _ in range(m)]
    tmp = []
    i, j = 0, 0
    while i < len(res) and j < len(a):
        if float(res[i][0]) < float(a[j][0]) \
          or float(res[i][0]) == float(a[j][0]) and res[i][1] > a[j][1]:
            tmp.append(a[j])
            j += 1
        else:
            tmp.append(res[i])
            i += 1
    tmp.extend(res[i:])
    tmp.extend(a[j:])
    res = tmp
print(len(res))
for i in res:
    print(*i)
