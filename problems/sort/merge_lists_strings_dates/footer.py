
#''' #  ЭТО не комментарий, а конец переменной source_code из header

#  валидация на содержание запрещённых инструкций
exclude_patterns = [r'\s*\.\s*sort', r'sorted\s*\(']

for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), 'You are using restricted constructions: list.sort, sorted'


exec(source_code)


L = input().split()
R = input().split()

A = merge_by_duration(L, R)

print(" ".join(A))
