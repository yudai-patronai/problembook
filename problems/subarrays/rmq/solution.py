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
        x, y = map(int, input().split())
        ans.append(str(calc(root, x, y)))
    print(" ".join(ans))
