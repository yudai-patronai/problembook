if __name__ == "__main__":
    n = int(input())
    stones = {}
    count = 0
    for c in map(int, input().strip().split()):
        stones[c] = stones.get(c, 0) + 1
        if stones[c] == 3:
            print(0)
            exit(0)
        if stones[c] == 2:
            count += 1
            if count == 2:
                print(0)
                exit(0)
    print(1)
