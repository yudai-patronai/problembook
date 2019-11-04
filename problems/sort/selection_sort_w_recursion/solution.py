#!/usr/bin/python3


def recursive_selection_sort(a):
    selection_sort(a, 0)


def selection_sort(a, index):
    if index < len(a) - 1:
        str_a  = ' '.join(map(str, a))
        min = find_min(a, index)
        a[index], a[min] = a[min], a[index]
        str_a_new = ' '.join(map(str, a))
        if str_a_new != str_a:
            str_a = str_a_new
            print(str_a)
        selection_sort(a, index + 1)


def find_min(a, index):
    min = index - 1
    if index < len(a) - 1:
        min = find_min(a, index + 1)
    if a[min] > a[index]:
        min = index
    return min

array = [int(e) for e in input().split()]
recursive_selection_sort(array)