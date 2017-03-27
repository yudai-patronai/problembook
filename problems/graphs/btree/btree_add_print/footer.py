

class JudgeTree:
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


def tree_def_str(node):
    if node is None:
        return '-'

    return '({} {} {})'.format(node.data, tree_def_str(node.left), tree_def_str(node.right))
        

if __name__ == "__main__":
    numbers = list(map(int, input().split()))

    JudgeTree.print = Tree.print
    jtree = JudgeTree()
    for x in numbers:
        jtree.add(x)

    jtree.print()
    print()

    tree = Tree()
    for x in numbers:
        tree.add(x)

    print(tree_def_str(tree.root))
