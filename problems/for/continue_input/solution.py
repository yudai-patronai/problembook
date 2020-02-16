def generate_answer(input_str):
    inputs = input_str.split('\n')
    s_prev = ''
    s_ret = ''
    while True:
        s = inputs.pop(0)
        if s == s_prev:
            break
        s_prev = s
        if not s:
            break
        if s[0].isupper():
            continue
        s_ret += s[0] + s[-1]
    return s_ret


if __name__ == "__main__":
    s_prev = ''
    s_ret = ''
    while True:
        s = input()
        if s == s_prev:
            break
        s_prev = s
        if not s:
            break
        if s[0].isupper():
            continue
        s_ret += s[0] + s[-1]
    print(s_ret)
