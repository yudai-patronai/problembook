def solution():
    string = input().strip()
    upper = 0
    lower = 0

    for symbol in string:
        if ord(symbol) >= ord('a') and ord(symbol) <= ord('z'):
            lower += 1
        elif ord(symbol) >= ord('A') and ord(symbol) <= ord('Z'):
            upper += 1

    return upper, lower

if __name__ == '__main__':
    upper, lower = solution()
    print(upper, lower)
