# import sys
# from io import StringIO


def bad_search(arr, x, is_greater):
    l = -1
    for i in range(len(arr)):
        if is_greater(x, arr[i]):
            l += 1
        else:
            break
    r = l + 1
    for i in range(r, len(arr)):
        if is_greater(arr[i], x):
            break
        else:
            r += 1
    return l, r


def parse_time(s):
    hours, mins, secs = s.split(':')
    secs, msecs = secs.split('.')
    return 3600000 * int(hours) + 60000 * int(mins) + 1000 * int(secs) + int(msecs)


def parse_entry(s):
    time, t = s.split()
    time = parse_time(time)
    return time, t


def is_greater_by_time(e1, e2):
    return e1[0] > e2[0]


def find_types(logs, key):
    res = []
    l, r = bad_search(logs, (key, ''), is_greater_by_time)
    print(l, r)
    for i in range(l + 1, r):
        res.append(logs[i][1])
    if l + 1 == r:
        # Not found
        if l >= 0:
            need_time = logs[l][0]
            for i in range(l, -1, -1):
                if logs[i][0] == need_time:
                    res.append(logs[i][1])
        if r < len(logs):
            need_time = logs[r][0]
            for i in range(r, len(logs)):
                if logs[i][0] == need_time:
                    res.append(logs[i][1])
    return res


'''def check_test(filename, bad=False):
    search = bad_binary_search if bad else good_binary_search
    # old_stdout = sys.stdout
    # sys.stdout = StringIO()
    old_stdin = sys.stdin
    with open('tests/{}'.format(filename), 'r') as f:
        sys.stdin = f
        __start(search)
    sys.stdin = old_stdin
    # sys.stdout = old_stdout
'''

logs = []
while True:
    entry = input()
    if entry == '#':
        break
    logs.append(parse_entry(entry))
key = parse_time(input())
print(*sorted(find_types(logs, key)))
