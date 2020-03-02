import os
import random
import shutil
import math
from collections import namedtuple


EPS = 1e-5
random.seed(46)
Point = namedtuple("Point", ["x", "y"])


def get_ang(p, q, r):
    v = Point(q.x - p.x, q.y - p.y)
    w = Point(r.x - q.x, r.y - q.y)
    dot = v.x*w.x + v.y*w.y
    l1 = (v.x*v.x + v.y*v.y) ** 0.5
    l2 = (w.x*w.x + w.y*w.y) ** 0.5
    ang = math.acos(round(dot / l1 / l2, 5))
    if ang < 0:
        ang += math.pi * 2
    return ang


def check(p, q, r):
    v = Point(q.x - p.x, q.y - p.y)
    w = Point(r.x - q.x, r.y - q.y)
    cross = v.x*w.y - v.y*w.x
    return cross > EPS


def dist(p, q):
    return ((p.x - q.x)**2 + (p.y - q.y)**2) ** 0.5


def rotate_and_normalize(p, q, a):
    v = Point(q.x - p.x, q.y - p.y)
    vl = (v.x*v.x + v.y*v.y) ** 0.5
    return [
        round((math.cos(a) * v.x - math.sin(a) * v.y) / vl, 5),
        round((math.sin(a) * v.x + math.cos(a) * v.y) / vl, 5)
    ]


def generate_convex_polygon(max_size):
    size = 2
    poly = [Point(round(random.random() * 1500 - 1000, 5),
                  round(random.random() * 1500 - 1000, 5)),
            Point(round(random.random() * 500 + 500, 5),
                  round(random.random() * 500 + 500, 5))]
    lower = math.radians(3)
    while size < max_size:
        upper = min(math.radians(30), get_ang(poly[-2], poly[-1], poly[0]))
        if upper - lower < 0:
            break
        ang = random.random() * (upper - lower) + lower
        v = rotate_and_normalize(poly[-2], poly[-1], ang)
        lim = 100
        p = None
        while p is None:
            d = random.random() * lim + 1
            p = Point(round(poly[-1].x + v[0] * d, 5),
                      round(poly[-1].y + v[1] * d, 5))
            if not check(p, poly[0], poly[1]):
                lim = d - 0.5
                p = None
        poly.append(p)
        size += 1
        if dist(p, poly[0]) - 10 < -EPS:
            break
    return poly


def check2(p, q, r):
    v = Point(q.x - p.x, q.y - p.y)
    w = Point(r.x - p.x, r.y - p.y)
    cross = v.x*w.y - v.y*w.x
    return cross > EPS


def solve(poly, p):
    for i in range(-1, len(poly) - 1):
        if not check2(poly[i], poly[i+1], p):
            return "NO"
    return "YES"


def generate_test(name, testn, inside=False):
    n = random.randint(50, 1000)
    poly = generate_convex_polygon(n)
    points = ["{:.5f} {:.5f}".format(p.x, p.y) for p in poly]
    if inside:
        j = i = random.randint(0, len(poly) - 1)
        while j == i:
            j = random.randint(0, len(poly) - 1)
        p = Point(round((poly[i].x + poly[j].x) / 2.0, 5),
                  round((poly[i].y + poly[j].y) / 2.0, 5))
    else:
        p = Point(round(random.random() * 2000 - 1000, 5),
                  round(random.random() * 2000 - 1000, 5))
    ans = solve(poly, p)
    with open(name, "w") as f:
        f.write(str(len(points)) + "\n")
        f.write("\n".join(points) + "\n")
        f.write("{:.5f} {:.5f}\n".format(p.x, p.y))
    with open(name+".a", "w") as f:
        f.write(ans)


def mantest(name, queries, answer):
    with open(name, "w") as f:
        f.write("\n".join(queries) + "\n")
    with open(name+".a", "w") as f:
        f.write(answer)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    test = 1
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    mantest(
        test_name,
        [
            "4",
            "1 1",
            "0 1",
            "0 0",
            "1 0",
            "0.5 0.5"
        ],
        "YES"
    )

    test = 2
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    mantest(
        test_name,
        [
            "3",
            "0 1",
            "-1 1",
            "-1 -1",
            "0 0"
        ],
        "NO"
    )

    test = 3
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    mantest(
        test_name,
        [
            "5",
            "-1 3",
            "-2 1",
            "-1 -1",
            "3 -2",
            "2 2",
            "-2 1"
        ],
        "YES"
    )

    test = 4
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    mantest(
        test_name,
        [
            "5",
            "-1 3",
            "-2 1",
            "-1 -1",
            "3 -2",
            "2 2",
            "2.5 0"
        ],
        "YES"
    )

    for test in range(5, 7):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)

    test = 7
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    generate_test(test_name, test, True)
