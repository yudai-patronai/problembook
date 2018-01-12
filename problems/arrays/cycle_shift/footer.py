def solution(arr):
    return arr[1:]+arr[:1]


if __name__ == "__main__":
    array = [int(x) for x in input().split(" ")]
    array_test = array[:]
    cycle_shift(array, len(array))
    array_test = solution(array_test)
    assert array == array_test, """
    Your function doesn't change the input array properly!
    """
    print(" ".join(map(str, array)))
