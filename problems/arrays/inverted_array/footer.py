#!/usr/bin/env python3

if __name__ == "__main__":
    array = [int(x) for x in input().split(" ")]
    array_test = array[:]
    N = int(input())
    reversed = invert_array(array, N)
    assert array == array_test, "Your function changes the input array!"
    print(" ".join(map(str, reversed)))
