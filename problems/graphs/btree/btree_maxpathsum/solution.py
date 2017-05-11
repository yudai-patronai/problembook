#!/usr/bin/env python3
import sys


class Node:
    def __init__(self, data):
        self.data = data  # данные в узле
        self.left = None
        self.right = None


def wh(node):
    if node is None:
        return 0

    return max(wh(node.left), wh(node.right)) + node.data


def read_tree():
    n = int(input())
    ar = [Node(0) for _ in range(n)]
    for i in range(n):
        data, left, right = map(int, input().split())
        ar[i].data = data
        if left != -1:
            ar[i].left = ar[left]
        if right != -1:
            ar[i].right = ar[right]

    return ar[0]


def solve(node, output_file=sys.stdout):
    output_file.write(str(wh(node)) + '\n')


if __name__ == '__main__':
    solve(read_tree())
