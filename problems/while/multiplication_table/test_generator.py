import os
import shutil

from lib.testgen import TestSet


N = 9


def get_table(N):
    table = ""
    lines = []

    for i in range(1, N+1):
        line = "# "
        for j in range(1, N+1):
            ans = str(j * i)
            ans = ans if len(ans) == 2 else "0" + ans
            line += str(i) + " x " + str(j) + " = " + ans\
                 + (" | " if j != N else " ")

        line += "#"
        lines.append(line)

    table += (len(lines[0]) * "#") + "\n"
    table += "\n".join(lines)
    table += "\n" + (len(lines[0]) * "#")

    return table


def main():
    tests = TestSet()

    for i in range(1, N+1):
        table = get_table(i)
        tests.add(
            str(i) + "\n",
            str(table)  + "\n"
        )


if __name__ == "__main__":
    main()
