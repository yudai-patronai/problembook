from math import ceil


def sift_down(heap, i):
    n = len(heap)
    while 2*i+1 < n:
        j = i
        if heap[2*i+1] < heap[i]:
            j = 2*i+1
        if 2*i+2 < n and heap[2*i+2] < heap[j]:
            j = 2*i+2
        if i == j:
            break
        heap[i], heap[j] = heap[j], heap[i]
        i = j


def build_heap(heap):
    n = len(heap)
    for i in range(ceil(n/2), -1, -1):
        sift_down(heap, i)


if __name__ == "__main__":
    n = int(intput())
    a = list(map(int, input().split()))
    build_heap(a)
    print(" ".join(map(str, a)))
