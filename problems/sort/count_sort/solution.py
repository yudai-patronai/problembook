def count_sort(A):
    cardinality = 10
    quantities = [0] * cardinality
    for x in A:
        quantities[x] += 1
        print(' '.join(map(str, quantities)))

    pos = 0
    for x in range(0, cardinality):
        for i in range(quantities[x]):
            A[pos] = x
            pos += 1

    return quantities

#  array of digits
array = list(map(int, input().split()))
quantities = count_sort(array)

#print(' '.join(map(str, quantities)))
print(' '.join(map(str, array)))
