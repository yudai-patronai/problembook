if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    for i in reversed(range(1, n)):
        if a[(i-1)//2] < a[i]:
            print("NO")
            break
    else:
        print("YES")
