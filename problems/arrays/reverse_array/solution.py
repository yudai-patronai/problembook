#!/usr/bin/env python3

def reverse_array(arr, N):
    for i in range(N//2):
        arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
