import os
import random
import shutil
import math
from collections import namedtuple

EPS = 1e-5
random.seed(42)
Point = namedtuple("Point", ["x", "y"])


def get_ang(p, q, r):
    v = Point(q.x - p.x, q.y - p.y)
    w = Point(r.x - q.x, r.y - q.y)
    dot = v.x*w.x + v.y*w.y
    l1 = (v.x*v.x + v.y*v.y) ** 0.5
    l2 = (w.x*w.x + w.y*w.y) ** 0.5
    return math.acos(round(dot / l1 / l2, 5))


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
    lower = math.radians(15)
    while size < max_size:
        sweep = max(math.pi/2, get_ang(poly[-2], poly[-1], poly[0])) - lower
        if sweep < 0:
            break
        ang = random.random() * sweep + lower
        v = rotate_and_normalize(poly[-2], poly[-1], ang)
        lim = 400
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


def get_area(poly):
    ans = 0
    for i in range(-1, len(poly) - 1):
        v = poly[i]
        w = poly[i + 1]
        ans += (v.x*w.y - v.y*w.x) / 2
    return round(abs(ans), 5)


def generate_test(name, testn):
    n = random.randint(3, 90)
    m = random.randint(1, 10)
    poly = generate_convex_polygon(n)
    queries = ["end"]
    answers = []
    while poly:
        action = "add"
        if len(poly) > 1 and m > 0:
            action = (["area"] + ["add"] * 8)[random.randint(0, 99) % 9]
        if action == "add":
            j = random.randint(0, len(poly) - 1)
            queries.append("add {} {} {}".format(j, poly[j].x, poly[j].y))
            poly.pop(j)
        else:
            m -= 1
            queries.append("area")
            answers.append(str(get_area(poly)))
    with open(name, "w") as f:
        f.write("\n".join(reversed(queries)) + "\n")
    with open(name+".a", "w") as f:
        f.write("\n".join(reversed(answers)))


def generate_max_test(name, testn):
    n = 90
    m = 10
    poly = generate_convex_polygon(n)
    queries = ["end"]
    answers = []
    while poly:
        action = "add"
        if len(poly) > 1 and m > 0:
            action = (["area"] + ["add"] * 8)[random.randint(0, 99) % 9]
        if action == "add":
            j = random.randint(0, len(poly) - 1)
            queries.append("add {} {} {}".format(j, poly[j].x, poly[j].y))
            poly.pop(j)
        else:
            m -= 1
            queries.append("area")
            answers.append(str(get_area(poly)))
    with open(name, "w") as f:
        f.write("\n".join(reversed(queries)) + "\n")
    with open(name+".a", "w") as f:
        f.write("\n".join(reversed(answers)))


def mantest(name, queries, answers):
    with open(name, "w") as f:
        f.write("\n".join(queries) + "\n")
    with open(name+".a", "w") as f:
        f.write("\n".join(answers))


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
            "add 0 1 1",
            "add 1 0 1",
            "add 2 0 0",
            "area",
            "add 3 1 0",
            "area",
            "end"
        ],
        [
            "0.5",
            "1"
        ]
    )

    test = 2
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    mantest(
        test_name,
        [
            "add 0 0 1",
            "add 1 -1 1",
            "add 1 -1 -1",
            "area",
            "end"
        ],
        [
            "1"
        ]
    )

    test = 3
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    mantest(
        test_name,
        [
            "add 0 -1 3",
            "add 1 2 2",
            "add 2 -1 -1",
            "area",
            "add 2 3 -2",
            "area",
            "add 4 -2 1",
            "area",
            "end"
        ],
        [
            "6",
            "13.5",
            "15.5"
        ]
    )

    for test in range(4, 7):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)

    test = 7
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    generate_max_test(test_name, test)
