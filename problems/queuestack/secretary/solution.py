def count(string):
    stack = []

    for token in string.split():

        if token.isdigit():
            stack.append(float(token))
        elif token[0] == '-' and len(token) > 1:
            stack.append(float(token))
        elif token == '#':
            if len(stack) > 0:
                res = sum(stack)
                stack = []
                stack.append(res)
            else:
                return 0.0
        elif token == '%':
            if len(stack) < 2:
                return 0.0
            else:
                res = stack.pop()
                stack.append(stack.pop()*res*0.01)
    if len(stack) > 0:
        return stack[-1]
    else:
        return 0.0


if __name__ == "__main__":
    print(count(input()))
