#''' # ЭТО не комментарий, а конец переменной source_code из header

# валидация на содержание запрещённых инструкций
exclude_patterns = [r'\s*\.\s*append', r'\s*\.\s*sort', r'sorted']

for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), \
        'You are using restricted constructions'

exec(source_code)  # объект merge_sort становится доступен

# Считывание данных с учётом того, что могут быть пустые массивы
A = list(map(int, input().split()))

# Запуск функции и проверка её на inplace
id_before = id(A)
merge_sort(A)
id_after = id(A)
assert id_before == id_after, 'Your function does not work inplace'

# Блок проверки рекурсии
if len(A) > 1:
    # Временное перенаправление потока вывода,
    # потому что во время проверки рекурсии запустятся
    # print-ы в merge_sort.
    old_stdout, sys.stdout = sys.stdout, StringIO()
    assert test_recursion(lambda: merge_sort(A)), \
        'Your function must be recursive'
    sys.stdout = old_stdout
