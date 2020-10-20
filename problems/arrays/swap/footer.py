
def correct_swap(arr, k):
    edge = len(arr) - len(arr) % k
    for i in range(0, edge, 2*k):
        for j in range(i, i+k):
            if j + k < len(arr):
                arr[j], arr[j+k] = arr[j+k], arr[j]


if __name__ == "__main__":
    # _ = input()
    array_input = input().split()
    k = int(input())

    array_input_str_before = str(array_input)

    array_correct = list(array_input)  # copy

    swap(array_input, k)  # student's answer
    correct_swap(array_correct, k)  # correct answer

    assert array_input == array_correct, """
    Your function doesn't change the input array properly:\nInput: {}\nSolution: {}\nCorrect: {}
    """.format(array_input_str_before, array_input, array_correct)
    print(' '.join(array_correct))
