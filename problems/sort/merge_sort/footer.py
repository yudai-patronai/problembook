
#''' # ЭТО не комментарий, а конец переменной source_code из header

# валидация на содержание запрещённых инструкций
exclude_patterns = [r'\s*\.\s*append', r'\s*\.\s*sort', r'sorted']

for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), 'You are using restricted constructions'


exec(source_code)

#  считывание данных с учётом того, что могут быть пустые массивы
A = list(map(int, input().split()))
id_before = id(A)
merge_sort(A)
id_after = id(A)

assert id_before == id_after, 'Your function does not work inplace'
