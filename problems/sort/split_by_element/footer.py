if __name__ == "__main__":
    array = [int(x) for x in input().split(" ")]
    x = int(input())
    n = len(array)
    split_array(array, n, x)
    print(" ".join(map(str, array)))
