
#''' # ЭТО не комментарий, а конец переменной source_code из header

# валидация на содержание запрещённых инструкций
exclude_patterns = ['append', 'sort', 'sorted']

for pattern in exclude_patterns:
    reobj = re.compile(pattern)
    assert not re.findall(reobj, source_code), 'instruction "{}" could not be used'.format(pattern)


exec(source_code)  # объект merge(L, R) становится доступным

#  считывание данных с учётом того, что могут быть пустые массивы
L = input().split()
R = input().split()

L = list(map(int, L)) if L else []
R = list(map(int, R)) if R else []

A = merge(L, R)

print(' '.join(map(str, A)))
