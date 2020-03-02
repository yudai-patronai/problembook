from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
EPS = 1e-5


def check(p, q, r):
    v = Point(q.x - p.x, q.y - p.y)
    w = Point(r.x - q.x, r.y - q.y)
    cross = v.x*w.y - v.y*w.x
    return cross > EPS or abs(cross) < EPS


if __name__ == "__main__":
    n = int(input())
    poly = []
    for _ in range(n):
        x, y = map(float, input().strip().split())
        poly.append(Point(x, y))
    x, y = map(float, input().strip().split())
    p = Point(x, y)
    for i in range(-1, len(poly) - 1):
        if not check(poly[i], poly[i+1], p):
            print("NO")
            break
    else:
        print("YES")
