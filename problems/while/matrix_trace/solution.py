def solution():
    trace = 0.0
    N = int(input())
    for i in range(N):
        trace += int(input().split()[i])

    return trace


if __name__ == "__main__":
    print(solution())
