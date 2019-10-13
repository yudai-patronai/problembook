import os
import shutil


N = 50
TEST_PATH = "tests"


def get_triangle(N):
    triangle = ""
    counter = 1
    for i in range(1, N+1):
        for _ in range(i):
            triangle += str(counter) + " "
            counter += 1
        triangle += "\n"

    return triangle[:-1]


def main():
    shutil.rmtree(TEST_PATH, ignore_errors=True)
    os.mkdir(TEST_PATH)

    for i in range(1, N):
        triangle = get_triangle(i)
        with open(os.path.join(TEST_PATH, str(i)), "w") as f:
            f.write(str(i))

        with open(os.path.join(TEST_PATH, str(i) + ".a"), "w") as f:
            f.write(triangle)


if __name__ == "__main__":
    main()