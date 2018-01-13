def solution(arr):
    N = len(arr)
    sseq_len = []
    for i in range(N):
        subseq = [el for idx, el in enumerate(sseq_len) if arr[idx] < arr[i]]
        if subseq:
            sseq_len.append(max(subseq) + 1)
        else:
            sseq_len.append(1)
    return max(sseq_len)


arr = [int(i) for i in input().strip().split(' ')]
print(solution(arr))
