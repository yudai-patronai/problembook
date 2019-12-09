
#''' #  ЭТО не комментарий, а конец переменной source_code из header

#  валидация на содержание запрещённых инструкций
exclude_patterns = [r'\.\s*sort\s*\(', r'sorted\s*\(']

for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), 'list.sort() and sorted() are restricted'


exec(source_code)

A = input().split(';')

id_before = id(A)
split_barrier(A)
id_after = id(A)

assert id_before == id_after, 'Your function does not work INPLACE'

print(';'.join(map(str, A)))
