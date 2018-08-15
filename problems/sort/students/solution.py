N = int(input())
lst = [[] for _ in range(N)]

while True:
    raw = input().strip()
    if raw == '#':
        break

    student_id, value = list(map(int, raw.split()))
    lst[student_id].append(value)

lst = [sorted(sub_list, reverse=True) for sub_list in lst]
lst.sort(key=lambda x: sum(x), reverse=True)
lst_str = [' '.join(list(map(str, x))) for x in lst]

print(' '.join(lst_str))
