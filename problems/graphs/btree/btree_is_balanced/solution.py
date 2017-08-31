#!/usr/bin/env python3
import sys


class Node:
    def __init__(self, data):
        self.data = data  # данные в узле
        self.left = None
        self.right = None

    def height(self):
        if self.left is None:
            h = 0
        else:
            h = self.left.height()

        if self.right is not None:
            h = max(h, self.right.height())

        return h + 1


def is_balanced(node):
    if node is None:
        return True, 0

    lb, lh = is_balanced(node.left)
    rb, rh = is_balanced(node.right)

    return lb and rb and abs(lh - rh) <= 1, 1 + max(lh, rh)


class Tree:
    def __init__(self, sequence=None):
        self.root = None

        if sequence:
            for x in sequence:
                self.add(x)

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

    def is_balanced(self):
        return is_balanced(self.root)[0]


def str_numbers(sequence):
    return ' '.join(map(str, sequence))


def input_numbers():
    return map(int, input().split())


def solve(sequence, output_file=sys.stdout):
    output_file.write('YES\n' if Tree(sequence).is_balanced() else 'NO\n')


if __name__ == '__main__':
    solve(input_numbers())
