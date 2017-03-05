#!/usr/bin/env python3
import os
import sys

sys.path.append(os.path.abspath('../..'))
import task

def dfs_cycle_x(graph, x):
    '''
    white - not yet working with it(may already be in stack though)
    gray - started working with it, searching it's children now
    black - finished working with it, all it's children are black
    '''
    black = set()
    gray = set()
    parent = [-1] * len(graph)
    loop_found = False

    stack = [x]
    while stack:
        v = stack[-1]
        if v in black:
            ''' Have found it deeper already '''
            stack.pop()
            continue
        if v in gray:
            gray.remove(v)
            black.add(v)
            stack.pop()
            continue

        gray.add(v)
        for n in graph[v]:
            if n in black:
                continue
            elif n in gray:
                stack = []
                loop_found = True
                break
            else:
                parent[n] = v
                stack.append(n)

    if loop_found:
        l = [v]
        while l[-1] != n:
            if parent[l[-1]] == -1:
                raise Exception('Cicle resolution problem')
            l.append(parent[l[-1]])

        return l[::-1], None

    return [], black

def solve(graph):
    black = set()
    for x in range(len(graph)):
        ''' Iterate all connectiviti components '''
        if x in black:
            continue
        c, b = dfs_cycle_x(graph, x)
        if c:
            return ' '.join(map(str, c)) + '\n'
        if b:
            black |= b
    return 'YES\n'

if __name__ == "__main__":
    n, m, g = task.read_task_directed()
    print(solve(g), end='')
