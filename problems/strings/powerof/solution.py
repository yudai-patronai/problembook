def solution(string, exponent):
    if exponent > 0:
        return string * exponent

    exponent = -exponent
    if len(string) % exponent != 0:
        return 'NO SOLUTION'

    base = string[:len(string) // exponent]
    return base if base * exponent == string else 'NO SOLUTION'


if __name__ == '__main__':
    string = input().strip()
    exponent = int(input())
    print(solution(string, exponent))
