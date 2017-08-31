#!/usr/bin/env python3

from lib.graphs import task


def _hamilton(g, Visited, Path, curr):
    Path.append(curr)
    if len(Path) == len(g):
        if Path[0] in g[Path[-1]]:
            return True
        else:
            Path.pop()
            return False

    Visited[curr] = True
    for next in g[curr]:
        if not Visited[next]:
            if _hamilton(g, Visited, Path, next):
                return True
    Visited[curr] = False
    Path.pop()

    return False


def hamilton(g, curr):
    Visited = [False] * len(g)
    Path = []
    if _hamilton(g, Visited, Path, curr):
        return Path
    return None


def solve(graph):
    return ' '.join(map(str, hamilton(graph, 0))) + '\n'


if __name__ == "__main__":
    n, m, g = task.read_task()
    print(solve(g), end='')
