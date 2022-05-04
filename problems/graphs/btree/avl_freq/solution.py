class Node:
    def __init__(self, key):
        self.key = key
        self.value = 1
        self.height = 1
        self.left = self.right = None

class FreqTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        self.root = FreqTree._add(self.root, key)

    def __str__(self):
        array = []
        FreqTree._flatten(self.root, array)
        return "\n".join(array)

    @staticmethod
    def _add(node, key):
        if node is None:
            return Node(key)
        if node.key == key:
            node.value += 1
            return node
        elif node.key < key:
            node.right = FreqTree._add(node.right, key)
            node.height = max(FreqTree._height(node.left), FreqTree._height(node.right)) + 1
            return FreqTree._rotate(node)
        else:
            node.left = FreqTree._add(node.left, key)
            node.height = max(FreqTree._height(node.left), FreqTree._height(node.right)) + 1
            return FreqTree._rotate(node)

    @staticmethod
    def height(node):
        if node:
            return node.height
        else:
            return 0

    @staticmethod
    def _rotate_right(node):
        left = node.left
        c = left.right
        node.left = c
        node.height = max(FreqTree._height(node.right), FreqTree._height(c)) + 1
        left.right = node
        left.height = max(FreqTree._height(left.left), FreqTree._height(node)) + 1
        return left

    @staticmethod
    def _rotate_left(node):
        right = node.right
        c = right.left
        node.right = c
        node.height = max(FreqTree._height(node.left), FreqTree._height(c)) + 1
        right.left = node
        right.height = max(FreqTree._height(right.right), FreqTree._height(node)) + 1
        return right

    @staticmethod
    def _rotate(node):
        left = node.left
        h_left = FreqTree._height(left)
        right = node.right
        h_right = FreqTree._height(right)
        if h_left + 1 < h_right:
            c = right.left
            if FreqTree._height(c) <= FreqTree._height(right.right):
                return FreqTree._rotate_left(node)
            else:
                node.right = FreqTree._rotate_right(right)
                node.height = max(h_left, FreqTree._height(node.right))
                return FreqTree._rotate_left(node)
        elif h_right + 1 < h_left:
            c = left.right
            if FreqTree._height(c) <= FreqTree._height(left.left):
                return FreqTree._rotate_right(node)
            else:
                node.left = FreqTree._rotate_left(left)
                node.height = max(h_right, FreqTree._height(node.left))
                return FreqTree._rotate_right(node)
        else:
            return node

    @staticmethod
    def _flatten(node, array):
        if node is None:
            return
        FreqTree._flatten(node.left, array)
        array.append("{} {}".format(node.key, node.value))
        FreqTree._flatten(node.right, array)


if __name__ == "__main__":
    ft = FreqTree()
    items = map(int, input().split())
    for item in items:
        ft.add(item)
    print(ft)
