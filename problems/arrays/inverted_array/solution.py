#!/usr/bin/env python3

def invert_array(arr, N):
    return list() if N == 0 else arr[N-1::-1]
