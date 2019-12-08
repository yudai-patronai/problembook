def binary_search_right(arr, x, is_greater):
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if is_greater(arr[mid], x):
            right = mid
        else:
            left = mid
    return right


def binary_search_left(arr, x, is_greater):
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if is_greater(x, arr[mid]):
            left = mid
        else:
            right = mid
    return left


def binary_search(arr, x, is_greater):
    return binary_search_left(arr, x, is_greater), binary_search_right(arr, x, is_greater)


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
    l, r = binary_search(logs, (key, ''), is_greater_by_time)
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


logs = []
while True:
    entry = input()
    if entry == '#':
        break
    logs.append(parse_entry(entry))
key = parse_time(input())
print(*sorted(find_types(logs, key)))
