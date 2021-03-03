class Node:
    def __init__(self, value, segm):
        self.value = value
        self.segm = segm
        self.left = self.right = None


def build_tree(a, f, t):
    if f == t:
        node = Node(a[f], (f, f))
        return node
    x = build_tree(a, f, (f+t)//2)
    y = build_tree(a, (f+t)//2+1, t)
    node = Node(max(x.value, y.value), (f, t))
    node.left = x
    node.right = y
    return node


def update(node, i, value):
    if i < node.segm[0] or i > node.segm[1]:
        return node.value
    if node.segm[0] == node.segm[1]:
        node.value = value
        return value
    x = update(node.left, i, value)
    y = update(node.right, i, value)
    node.value = max(x, y)
    return node.value


def calc(node, f, t):
    if f <= node.segm[0] and node.segm[1] <= t:
        return node.value
    if t < node.segm[0] or node.segm[1] < f:
        return float("-inf")
    x = calc(node.left, f, t)
    y = calc(node.right, f, t)
    return max(x, y)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    root = build_tree(a, 0, n-1)
    k = int(input())
    ans = []
    for _ in range(k):
        cmd, x, y = input().split()
        x = int(x)
        y = int(y)
        if cmd == "upd":
            update(root, x, y)
        else:
            ans.append(str(calc(root, x, y)))
    print(" ".join(ans))
