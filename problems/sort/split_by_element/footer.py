
#''' #  ЭТО не комментарий, а конец переменной source_code из header

#  валидация на содержание запрещённых инструкций
exclude_patterns = [r'\.sort', r'sorted']

for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), 'instruction "{}" could not be used'.format(pattern)


exec(source_code)

A = list( map(int, input().split()) )
barrier = int(input())

id_before = id(A)
split_barrier(A, barrier)
id_after = id(A)

assert id_before == id_after, 'Your function does not work INPLACE'

print(' '.join(map(str, A)))
