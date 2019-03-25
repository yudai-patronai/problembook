if __name__ == "__main__":
    g = map(int, input().strip().split())
    a = 0.0
    for k, p in zip(g, [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]):
        a += k * p * 2
    print(a)
