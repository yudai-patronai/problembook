#!/usr/bin/env python3

from lib.graphs import task


class HamCycle():
    def __init__(self, Cycle=None, CycleLen=0):
        self.Cycle = Cycle
        self.CycleLen = CycleLen


def _voyager(g, Used, Path, PathLen, Opti, curr):
    Path.append(curr)
    if len(Path) == len(g):
        if Path[0] in g[Path[-1]]:
            CycleLen = PathLen + g[Path[-1]][Path[0]]
            if Opti.Cycle == None or CycleLen < Opti.CycleLen:
                Opti.Cycle = Path[:]
                Opti.CycleLen = CycleLen
        Path.pop()
        return

    Used.add(curr)
    for next, w in g[curr].items():
        if next not in Used:
            _voyager(g, Used, Path, PathLen + w, Opti, next)
    Used.remove(curr)
    Path.pop()
    return


def voyager(g, curr):
    Used = set()
    Path = []
    PathLen = 0
    Opti = HamCycle()
    _voyager(g, Used, Path, PathLen, Opti, curr)
    return Opti.CycleLen, Opti.Cycle


def solve(graph):
    graph = [dict(l) for l in graph]
    CycleLen, Cycle = voyager(graph, 0)
    return str(CycleLen) + '\n' + ' '.join(map(str, Cycle)) + '\n'


if __name__ == "__main__":
    n, m, g = task.read_task_weight()
    print(solve(g), end='')
