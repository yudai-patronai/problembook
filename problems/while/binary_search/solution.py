#!/usr/bin/env python3

N = int(input())
K = int(input())
a = input()
a = [int(el) for el in a.split()]


def binary_search(seq, number):
    answer = -1
    left = 0
    right = len(seq) - 1
    while (left <= right):
        middle = (left + right) // 2
        if (seq[middle] == number):
            answer = middle + 1
            break
        elif (seq[middle] > number):
            right = middle - 1
        else:
            left = middle + 1
    return answer

print(binary_search(a, K))