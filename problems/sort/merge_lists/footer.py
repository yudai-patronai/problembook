#!/usr/bin/env python3

def solution(arr1, arr2):
    arr = []
    if len(arr1) == 0:
        arr = arr2[:]
        return arr
    if len(arr2) == 0:
        arr = arr1[:]
        return arr
    i1, i2 = 0, 0
    n1, n2 = len(arr1), len(arr2)
    while i1 < n1 and i2 < n2:
        if arr1[i1] < arr2[i2]:
            arr.append(arr1[i1])
            i1 += 1
        else:
            arr.append(arr2[i2])
            i2 += 1
    if i1 < n1:
        arr += arr1[i1:]
    if i2 < n2:
        arr += arr2[i2:]
    return arr

if __name__ == "__main__":
    arr1 = [int(x) for x in input().split(" ")]
    arr2 = [int(x) for x in input().split(" ")]
    array = merge_lists(arr1, arr2)
    array_test = solution(arr1, arr2)
    assert array == array_test, "Your function doesn't merge arrays properly!"
    print(" ".join(map(str, array)))