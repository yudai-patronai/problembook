#!/usr/bin/env python3
import os
import sys

sys.path.append(os.path.abspath('../..'))
import task

def dfs_topological_sort_x(graph, x, black):
    '''
    white - not yet working with it(may already be in stack though)
    gray - started working with it, searching it's children now
    black - finished working with it, all it's children are black
    '''
    gray = set()
    result = []
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
            result.append(v)
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
                stack.append(n)

    if loop_found:
        return None

    return result

def solve(graph):
    result = []
    black = set()
    for x in range(len(graph)):
        ''' Iterate all connectiviti components '''
        if x in black:
            continue
        r = dfs_topological_sort_x(graph, x, black)
        if not r:
            return 'NO\n'
        else:
            result.extend(r)
    return ' '.join(map(str, result[::-1])) + '\n'

if __name__ == "__main__":
    n, m, g = task.read_task_directed()
    print(solve(g), end='')
