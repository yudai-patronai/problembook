#!/usr/bin/env python3


if __name__ == "__main__":
    str = input()
    size = len(str)
    max = 0
    if size != 0:
        for i in range(size):
            j = i
            curr = 0
            while (j < size) and (str[j] == str[i]):
                curr = curr + 1
                j = j + 1
            if max < curr:
                max = curr
    print(max)
