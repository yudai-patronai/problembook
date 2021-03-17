class Node:
    def __init__(self, value, segm):
        self.value = value
        self.mod = 0
        self.segm = segm
        self.left = self.right = None


def build_tree(a, f, t):
    if f == t:
        node = Node(a[f], (f, f))
        return node
    x = build_tree(a, f, (f+t)//2)
    y = build_tree(a, (f+t)//2+1, t)
    node = Node(x.value + y.value, (f, t))
    node.left = x
    node.right = y
    return node


def total(node):
    return node.value + node.mod * (node.segm[1]-node.segm[0]+1)


def update(node, f, t, value):
    if t < node.segm[0] or node.segm[1] < f:
        return total(node)
    if f <= node.segm[0] and node.segm[1] <= t:
        node.mod += value
        return total(node)
    if node.mod != 0:
        node.left.mod += node.mod
        node.right.mod += node.mod
        node.mod = 0
    x = update(node.left, f, t, value)
    y = update(node.right, f, t, value)
    node.value = x + y
    return node.value


def calc(node, f, t):
    if f <= node.segm[0] and node.segm[1] <= t:
        return total(node)
    if t < node.segm[0] or node.segm[1] < f:
        return 0
    if node.mod != 0:
        node.left.mod += node.mod
        node.right.mod += node.mod
        node.mod = 0
        x = total(node.left)
        y = total(node.right)
        node.value = x + y
    x = calc(node.left, f, t)
    y = calc(node.right, f, t)
    return x + y


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    root = build_tree(a, 0, n-1)
    k = int(input())
    ans = []
    for _ in range(k):
        cmd, *args = input().split()
        args = map(int, args)
        if cmd == "add":
            update(root, *args)
        else:
            f, t = args
            res = calc(root, f, t) / (t - f + 1)
            ans.append("{:.3g}".format(res))
    print(" ".join(ans))
