def compute_z_function(s):
    z = [-1]
    left = right = 0
    for i in range(1, len(s)):
        x = min(z[i - left], right - i + 1) if i <= right else 0
        while i + x < len(s) and s[x] == s[i + x]:
            x += 1
        if i + x - 1 > right:
            left, right = i, i + x - 1
        z.append(x)
    return z


def solve(s):
    n = len(s)
    z = compute_z_function(s)
    i = 0
    for i in range(len(z)):
        if i + z[i] == n and i and not n % i:
            break

    return n // (n - z[i]) if i else 1


if __name__ == "__main__":
    s = input()

    if s:
        print(solve(s))
    else:
        print(1)
