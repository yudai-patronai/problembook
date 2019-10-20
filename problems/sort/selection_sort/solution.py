#!/usr/bin/python3


def selection_sort(a):
    str_a  = ' '.join(map(str, a))
    for i in range(0, len(a) - 1):
        min_j = i
        for j in range(i, len(a)):
            if a[j] < a[min_j]:
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]
        str_a_new = ' '.join(map(str, a))
        if str_a_new != str_a:
            str_a = str_a_new
            print(str_a)

array = [int(e) for e in input().split()]
selection_sort(array)
