#!/usr/bin/env python3
import sys


class Node:
    def __init__(self, data):
        self.data = data  # данные в узле
        self.left = None
        self.right = None


def mega_f(node):
    if node is None:
        return 0, 0

    l_h, l_d = mega_f(node.left)
    r_h, r_d = mega_f(node.right)

    return max(l_h, r_h) + 1, max(l_d, r_d, abs(l_h - r_h))


def disbalance(node):
    return mega_f(node)[1]


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
    output_file.write(str(disbalance(node)) + '\n')


if __name__ == '__main__':
    solve(read_tree())
