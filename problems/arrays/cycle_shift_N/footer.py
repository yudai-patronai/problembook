def solution(arr, N, M):
    M = M % N
    return arr[M:] + arr[:M]


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    array = [int(x) for x in input().split(" ")]
    array_test = array[:]
    cycle_shift_M(array, N, M)
    array_test = solution(array_test, N, M)
    assert array == array_test, """
    Your function doesn't change the input array properly!
    """
    print(" ".join(map(str, array)))
