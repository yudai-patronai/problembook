def replace_digs(s):
    out_s = ''
    replaces = {
        '0': 'ZERO',
        '1': 'ONE',
        '2': 'TWO',
        '3': 'THREE',
        '4': 'FOUR',
        '5': 'FIVE',
        '6': 'SIX',
        '7': 'SEVEN',
        '8': 'EIGHT',
        '9': 'NINE'
    }

    for c in s:
        if c == '_':
            break
        if c in [',', '.', '-']:
            continue
        if c in replaces:
            out_s += replaces[c]
            continue
        out_s += c
    return out_s


if __name__ == "__main__":
    s = input()
    out_s = replace_digs(s)
    print(out_s)
