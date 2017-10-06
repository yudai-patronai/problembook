#!/usr/bin/env python3

def solution(arr, N):
    for i in range(N//2):
        arr[i], arr[N-1-i] = arr[N-1-i], arr[i]


if __name__ == "__main__":
    array = [int(x) for x in input().split(" ")]
    array_test = array[:]
    N = int(input())
    reverse_array(array, N)
    solution(array_test, N)
    assert array == array_test, "Your function doesn't change the input array proprly!"
    print(" ".join(map(str, array)))
