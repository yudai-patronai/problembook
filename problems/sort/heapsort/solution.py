def max_heapify(A, heap_size, i):
    left = 2*i + 1
    right = 2*i + 2

    if left < heap_size and A[left] > A[i]:
        largest = left
    else:
        largest = i

    if right < heap_size and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, heap_size, largest)


def build_max_heap(A):
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, len(A), i)


def heapsort(A):
    build_max_heap(A)
    heap_size = len(A)
    print(*A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, heap_size, 0)
        print(*A)
