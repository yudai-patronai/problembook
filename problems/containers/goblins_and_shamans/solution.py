from math import ceil


def node(val):
    return {
        "value": val,
        "next": None
    }


def queue():
    return {
        "size": 0,
        "head": None,
        "tail": None
    }


def enqueue(queue, val):
    tmp = node(val)
    if not queue["size"]:
        queue["size"] = 1
        queue["head"] = queue["tail"] = tmp
        return
    queue["size"] += 1
    queue["tail"]["next"] = tmp
    queue["tail"] = tmp


def dequeue(queue):
    val = queue["head"]["value"]
    queue["head"] = queue["head"]["next"]
    queue["size"] -= 1
    if not queue["size"]:
        queue["tail"] = None
    return val


def insert(queue, pos, val):
    tmp = node(val)
    i = 0
    cur = queue["head"]
    while i != pos - 1:
        i += 1
        cur = cur["next"]
    tmp["next"] = cur["next"]
    cur["next"] = tmp
    queue["size"] += 1
    if tmp["next"] is None:
        queue["tail"] = tmp


if __name__ == "__main__":
    n = int(input())
    queue = queue()
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == "+":
            enqueue(queue, cmd[1])
        elif cmd[0] == "*":
            pos = ceil(queue["size"] / 2)
            if not pos:
                enqueue(queue, cmd[1])
            else:
                insert(queue, pos, cmd[1])
        else:
            print(dequeue(queue))
