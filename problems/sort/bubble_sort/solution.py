#!/usr/bin/python3


def bubbleSort(a):
    print(' '.join(map(str, a)))
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                print(' '.join(map(str, a)))


a = [int(element) for element in input().split()]
bubbleSort(a)
