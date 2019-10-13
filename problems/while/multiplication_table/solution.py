def solution():
    N = int(input())
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

    print(len(lines[0]) * "#")
    print("\n".join(lines))
    print(len(lines[0]) * "#")

if __name__ == "__main__":
    solution()