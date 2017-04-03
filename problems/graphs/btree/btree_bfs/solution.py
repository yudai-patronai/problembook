#!/usr/bin/env python3
import sys
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data  # данные в узле
        self.count = 1
        self.left = None
        self.right = None


class Tree:
    def __init__(self, sequence=None):
        self.root = None

        if sequence:
            for x in sequence:
                self.add(x)

    def add_at(self, node, data):
        if node.data == data:
            node.count += 1
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

    def print(self, output_file, node=None):
        if node is None:
            if self.root is None:
                return
            node = self.root

        if node.left is not None:
            self.print(output_file, node.left)

        output_file.write('{} {}\n'.format(node.data, node.count))

        if node.right is not None:
            self.print(output_file, node.right)


def bfs(node):
    ret = []

    if node is None:
        return ret

    queue = deque()
    queue.append(node)
    while queue:
        v = queue.popleft()
        ret.append(v)
        if v.left is not None:
            queue.append(v.left)
        if v.right is not None:
            queue.append(v.right)

    return ret


def solve(sequence, output_file):
    b = bfs(Tree(sequence).root)
    output_file.write(' '.join([str(n.data) for n in b]) + '\n')


if __name__ == '__main__':
    solve(map(int, input().split()), sys.stdout)
