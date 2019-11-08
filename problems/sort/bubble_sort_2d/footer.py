
#''' #  ЭТО не комментарий, а конец переменной source_code из header

#  валидация на содержание запрещённых инструкций
exclude_patterns = [
    r'\s*\.\s*sort',
    r'sorted\s*\(',
    r'\.\s*append',
    r'\.\s*pop',
    r'\[.*for.*\]', # list comprehension
    r'list\s*\(',   # list()
    r'\[\s*\]',
    r'\[.*:.*\]',   # slices
]

for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), 'You are using restricted constructions'


exec(source_code)

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append( list(map(int, input().split())) )

id_before = id(matrix)
bubble_sort2d(matrix, N, M)
id_after = id(matrix)

assert id_before == id_after, 'Your function does not work INPLACE'
