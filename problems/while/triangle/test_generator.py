import os
import shutil

from lib.testgen import TestSet

N = 50


def get_triangle(N):
    triangle = ""
    counter = 1
    for i in range(1, N+1):
        for _ in range(i):
            triangle += str(counter) + " "
            counter += 1
        triangle += "\n"

    return triangle


def main():
    tests = TestSet()

    for i in range(1, N):
        triangle = get_triangle(i)
        tests.add(
            str(i) + "\n",
            triangle
        )


if __name__ == "__main__":
    main()