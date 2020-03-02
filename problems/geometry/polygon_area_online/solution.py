from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def node(point):
    return {
        "val": point,
        "prev": None,
        "next": None
    }


def add(head, pos, point):
    tmp = node(point)
    if head is None:
        tmp["prev"] = tmp
        tmp["next"] = tmp
        return tmp
    if pos == 0:
        cur = head["prev"]
    else:
        j = 0
        cur = head
        while j != pos-1:
            j += 1
            cur = cur["next"]
    tmp["prev"] = cur
    tmp["next"] = cur["next"]
    cur["next"] = tmp
    tmp["next"]["prev"] = tmp
    if pos == 0:
        return tmp
    return head


def get_area(head):
    ans = 0
    cur = head
    while True:
        v = cur["val"]
        w = cur["next"]["val"]
        ans += v.x*w.y - v.y*w.x
        cur = cur["next"]
        if cur == head:
            break
    return abs(ans * 0.5)


if __name__ == "__main__":
    poly = None
    while True:
        cmd = input().split()
        if cmd[0] == "end":
            break
        elif cmd[0] == "add":
            poly = add(poly, int(cmd[1]), Point(*map(float, cmd[2:])))
        else:
            print(round(get_area(poly), 5))
