import os
import shutil

N = 9
TEST_PATH = "tests"


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
    shutil.rmtree(TEST_PATH, ignore_errors=True)
    os.mkdir(TEST_PATH)

    for i in range(1, N+1):
        table = get_table(i)
        with open(os.path.join(TEST_PATH, str(i)), "w") as f:
            f.write(str(i))
        
        with open(os.path.join(TEST_PATH, str(i) + ".a"), "w") as f:
            f.write(str(table))


if __name__ == "__main__":
    main()
