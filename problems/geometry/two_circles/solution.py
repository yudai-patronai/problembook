from math import sqrt

if __name__ == "__main__":
    x1, y1, r1 = [int(e) for e in input().split()]
    x2, y2, r2 = [int(e) for e in input().split()]
    r = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if r1 + r2 >= r and r + r2 >= r1 and r + r1 >= r2:
        print("YES")
    else:
        print("NO")
