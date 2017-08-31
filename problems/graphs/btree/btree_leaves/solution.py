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

    def height(self, node=None):
        if node is None:
            if self.root is None:
                return 0
            node = self.root

        return node.height()

    @staticmethod
    def do_leaves(leaves_list, node):
        if node.left is None and node.right is None:
            leaves_list.append(node.data)
            return

        if node.left is not None:
            Tree.do_leaves(leaves_list, node.left)

        if node.right is not None:
            Tree.do_leaves(leaves_list, node.right)

    def leaves(self, leaves_list=None, node=None):
        if self.root is None:
            return []

        leaves_list = []
        Tree.do_leaves(leaves_list, self.root)
        return leaves_list


def str_numbers(sequence):
    return ' '.join(map(str, sequence))


def input_numbers():
    return map(int, input().split())


def solve(sequence, output_file=sys.stdout):
    output_file.write(str_numbers(Tree(sequence).leaves()) + '\n')


if __name__ == '__main__':
    solve(input_numbers())
