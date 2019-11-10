def solve(n):
    arr = [0] * 10
    while n > 0:
        arr[n % 10] += 1
        n //= 10

    for i in range(1, 10):
        if arr[i] > 0:
            digit = str(i)
            arr[i] -= 1
            break

    return digit + \
        ''.join(map(lambda i: str(i) * arr[i], range(10)))


if __name__ == "__main__":
    print(solve(int(input())))
