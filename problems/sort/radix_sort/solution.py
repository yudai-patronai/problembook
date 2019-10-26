#!/usr/bin/python3

def radixSort(arrayToSort):
    n = len(arrayToSort)
    maxx = max(arrayToSort)
    p = 0
    while maxx > 0:
        p+=1
        maxx//=10
    for i in range(p):
        zero = []
        one =[]
        for j in range(n):
            if (arrayToSort[j] % 10**(i+1)) // (10**i) ==1:
                one.append(arrayToSort[j])
            else:
                zero.append(arrayToSort[j])
        arrayToSort = zero + one
        for i in arrayToSort:
            print(i, end = ' ')
        print()
inputArray = [int(element) for element in input().split()]
radixSort(inputArray)
