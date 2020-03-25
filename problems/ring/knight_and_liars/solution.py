def get_citizen(name, status):
    return {
        "name": name,
        "status": status,
        "next": None
        }


def insert(head, tail, name, status):
    tmp = get_citizen(name, status)
    if head is None:
        return tmp, tmp
    tmp["next"] = head
    tail["next"] = tmp
    return head, tmp


def kill(head, tail, prev):
    if id(prev) == id(tail):
        prev["next"] = prev["next"]["next"]
        return head["next"], tail
    if id(prev["next"]) == id(tail):
        prev["next"] = head
        return head, prev
    prev["next"] = prev["next"]["next"]
    return head, tail


def knightify(curr):
    curr["status"] = 1


def printisle(island1st, population):
    ptr = island1st
    for k in range(population):
        print(ptr["name"], ptr["status"])
        ptr = ptr["next"]


island1st = None
islandlast = None
population, news = tuple(map(int, input().split()))
for i in range(population):
    name, status = input().split()
    status = int(status)
    island1st, islandlast = insert(island1st, islandlast, name, status)
days = int(input())
curr = island1st
prev = islandlast
for j in range(days):
    if curr["status"] == 1:
        if news == 0:
            island1st, islandlast = kill(island1st, islandlast, prev)
            population -= 1
            curr = prev["next"]
        else:
            prev = prev["next"]
            curr = prev["next"]
    else:
        news = (news + 1) % 2
        if news == 1:
            knightify(curr)
            prev = prev["next"]
            curr = prev["next"]

        else:
            prev = prev["next"]
            curr = prev["next"]
    if population == 1:
        break
printisle(island1st, population)
