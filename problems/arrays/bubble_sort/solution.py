#!/usr/bin/python3


def bubble_sort(A):
    for k in range(1, len(A)):
        for i in range(0, len(A) - k):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]

n = int(input())
l = list(map(int, input().split()))
bubble_sort(l)
print(' '.join(map(str, l)))
