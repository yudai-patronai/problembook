
if __name__ == "__main__":
    array = [int(x) for x in input().split(" ")]
    x = int(input())
    n = len(array)
    l = e = g = 0
    for item in array:
        if item < x:
            l += 1
        elif item == x:
            e += 1
        else:
            g += 1
    ans = l
    split_array(array, n, x)
    for item in array:
        if item < x:
            l -= 1
        elif item == x:
            if l != 0:
                print(-1)
                exit(0)
            e -= 1
        else:
            if e != 0:
                print(-1)
                exit(0)
            g -= 1
    if l != 0 or e != 0 or g != 0:
        print(-1)
    else:
        print(ans)
