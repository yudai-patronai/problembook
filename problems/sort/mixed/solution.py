#!/usr/bin/python3

arr = list(map(int, input().split()))

for j in range(len(arr)):
    chg = 0
    pp = -1
    pn = -1
    for i in range(len(arr)):
        if arr[i] >= 0:
            if pp >= 0 and arr[i] < arr[pp]:
                arr[i], arr[pp] = arr[pp], arr[i]
                print(' '.join(map(str, arr)))
                chg += 1
            pp = i
        else:
            if pn >= 0 and arr[i] > arr[pn]:
                arr[i], arr[pn] = arr[pn], arr[i]
                print(' '.join(map(str, arr)))
                chg += 1
            pn = i
    if chg == 0:
        break
