
if __name__ == "__main__":
    array = [int(x) for x in input().split(" ")]
    array_test = array
    result = argsort(array, len(array))
    assert array == array_test, "Your function must not change array"
    assert len(array) == len(result), "Result array has different length!"
    print(" ".join(map(str, result)))
