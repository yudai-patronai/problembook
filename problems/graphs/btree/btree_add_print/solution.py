class Node:
    def __init__(self, data):
        self.data = data  # данные в узле
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add_at(self, node, data):
        if node.data == data:
            return

        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.add_at(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.add_at(node.right, data)

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        self.add_at(self.root, data)

    def print(self, node=None):
        if node is None:
            if self.root is None:
                return
            node = self.root

        if node.left is not None:
            self.print(node.left)
            print(' ', end='')

        print(node.data, end='')

        if node.right is not None:
            print(' ', end='')
            self.print(node.right)
