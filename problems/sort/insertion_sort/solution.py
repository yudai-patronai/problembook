#!/usr/bin/python3


def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            print(' '.join(map(str, A)))
            j = j - 1


array = [int(e) for e in input().split()]
insertion_sort(array)
