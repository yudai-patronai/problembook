#!/usr/bin/python3


def bubbleSort(arrayToSort):
    n = len(arrayToSort)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arrayToSort[j] > arrayToSort[j + 1] :
                arrayToSort[j], arrayToSort[j + 1] = arrayToSort[j + 1], arrayToSort[j]
                print(' '.join(map(str, arrayToSort)))

inputArray = [int(element) for element in input().split()]
bubbleSort(inputArray)
