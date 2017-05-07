#!/usr/bin/env python3
import sys


class Node:
    def __init__(self, data):
        self.data = data  # данные в узле
        self.left = None
        self.right = None


def mega_f(node):
    if node.left is None and node.right is None:
        return True, node.data, node.data

    if node.left is None:
        r_cor, r_min, r_max = mega_f(node.right)

        if not r_cor or r_min < node.data:
            return False, None, None

        return True, node.data, r_max

    if node.right is None:
        l_cor, l_min, l_max = mega_f(node.left)

        if not l_cor or l_max > node.data:
            return False, None, None

        return True, l_min, node.data

    l_cor, l_min, l_max = mega_f(node.left)
    r_cor, r_min, r_max = mega_f(node.right)

    if not (l_cor and r_cor):
        return False, None, None

    if l_max > node.data or r_min < node.data:
        return False, None, None

    return True, l_min, r_max


def is_corret(node):
    return mega_f(node)[0]


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
    output_file.write('YES\n' if is_corret(node) else 'NO\n')


if __name__ == '__main__':
    solve(read_tree())
