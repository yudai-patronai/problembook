def get_node(v):
    return {"value": v, "next": None}


def enqueue(head, tail, value):
    tmp = get_node(value)
    if head is None:
        return tmp, tmp
    tmp["next"] = head
    return tmp, tail


def dequeue(head, tail):
    if head is None:
        print("Stack is empty")
        return None, None, None
    if id(head) == id(tail):
        return None, None, head["value"]
    return head["next"], tail, head["value"]


def getop(golova, hvost):
    golova, hvost, op2 = dequeue(golova, hvost)
    golova, hvost, op1 = dequeue(golova, hvost)
    return golova, hvost, op1, op2


golova = None
hvost = None
a = input()

while a != '=':
    if a.isdigit():
        a = int(a)
        golova, hvost = enqueue(golova, hvost, a)
    elif a[0] == '-' and len(a) > 1:
        a = int(a)
        golova, hvost = enqueue(golova, hvost, a)
    elif a == '+':
        golova, hvost, op1, op2 = getop(golova, hvost)
        golova, hvost = enqueue(golova, hvost, op1 + op2)
    elif a == '-':
        golova, hvost, op1, op2 = getop(golova, hvost)
        golova, hvost = enqueue(golova, hvost, op1 - op2)
    elif a == '*':
        golova, hvost, op1, op2 = getop(golova, hvost)
        golova, hvost = enqueue(golova, hvost, op1 * op2)
    a = input()

head, tail, ans = dequeue(golova, hvost)
print(ans)
