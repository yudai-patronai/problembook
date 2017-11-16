def solution(arr):
    N = len(arr)
    subseq_len = []
    for i in range(N):
        subseq = [el for index, el in enumerate(subseq_len) if arr[index] < arr[i]]
        if subseq:
            subseq_len.append(max(subseq) + 1)
        else:
            subseq_len.append(1)
    return max(subseq_len)

arr = [int(i) for i in input().strip().split(' ')] 
print(solution(arr))