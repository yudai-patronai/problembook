def largest_rect(N, array):
    result = min(array) * N
    for w in range(1, N):
        for i in range(N - w + 1):
            result = max(result, min(array[i:i + w]) * w)
    return result
