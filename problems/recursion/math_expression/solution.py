# Tokens
END = 0
NUM = 1
OPEN = 2
CLOSE = 3
PLUS = 4
MINUS = 5
MUL = 6
DIV = 7
POW = 8

s = ""
p = 0


def next_token():
    global p
    if p == len(s):
        return END, 0
    c = s[p]
    p += 1
    if c == "(":
        return OPEN, 0
    elif c == ")":
        return CLOSE, 0
    elif c == "+":
        return PLUS, 0
    elif c == "-":
        return MINUS, 0
    elif c == "*":
        return MUL, 0
    elif c == "/":
        return DIV, 0
    elif c == "^":
        return POW, 0
    else:
        num = int(c)
        while p < len(s) and s[p].isdigit():
            num = num * 10 + int(s[p])
            p += 1
        return NUM, num


def lvl1(token, val):
    token, val = lvl2(token, val)
    while token == PLUS or token == MINUS:
        op = token
        token, rval = next_token()
        token, rval = lvl2(token, rval)
        if op == PLUS:
            val += rval
        else:
            val -= rval
    return token, val


def lvl2(token, val):
    token, val = lvl3(token, val)
    while token == MUL or token == DIV:
        op = token
        token, rval = next_token()
        token, rval = lvl3(token, rval)
        if op == MUL:
            val *= rval
        else:
            val //= rval
    return token, val


def lvl3(token, val):
    token, val = lvl4(token, val)
    while token == POW:
        token, rval = next_token()
        token, rval = lvl4(token, rval)
        val **= rval
    return token, val


def lvl4(token, val):
    if token == NUM:
        token, _ = next_token()
        return token, val
    elif token == MINUS:
        token, val = next_token()
        token, val = lvl3(token, val)
        return token, -val
    else:
        token, val = next_token()
        token, val = lvl1(token, val)
        token, _ = next_token()
        return token, val


s = input()
token, val = next_token()
_, val = lvl1(token, val)
print(val)
