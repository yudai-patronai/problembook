#!/usr/bin/env python3

from lib.graphs import task


def dfs_colored(g, start, black, white):
    for v in g[start]:
        if v in black | white:
            if len({start, v} & black) != 1:
                return False
        else:
            if start in black:
                white.add(v)
            else:
                black.add(v)
            if not dfs_colored(g, v, black, white):
                return False
    return True


def bigraph_group(g):
    black = set()
    white = set()

    for i in range(len(g)):
        if i not in black | white:
            black.add(i)
            if not dfs_colored(g, i, black, white):
                return []

    return list(black)


def solve(graph):
    cheaters = bigraph_group(graph)
    if len(cheaters):
        return ' '.join(map(str, cheaters)) + '\n'
    else:
        return 'NO\n'


if __name__ == "__main__":
    n, m, g = task.read_task()
    print(solve(g), end='')
