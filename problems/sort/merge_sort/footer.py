#''' # ЭТО не комментарий, а конец переменной source_code из header

# валидация на содержание запрещённых инструкций
# Отключено, т.к. ниже есть проверка на рекурсию.
# exclude_patterns = [r'\s*\.\s*append', r'\s*\.\s*sort', r'sorted']

# for reobj in exclude_patterns:
#     assert not re.findall(reobj, source_code), \
#         'You are using restricted constructions'

exec(source_code)  # объект merge_sort становится доступен

# Считывание данных с учётом того, что могут быть пустые массивы
A = list(map(int, input().split()))

# Запуск функции и проверка её на inplace
merge_sort(A)
is_inplace = all(A[i] <= A[i+1] for i in range(len(A) - 1))
assert is_inplace, 'Your function does not work inplace'

# Блок проверки рекурсии
if len(A) > 1:
    # Временное перенаправление потока вывода,
    # потому что во время проверки рекурсии запустятся
    # print-ы в merge_sort.
    old_stdout, sys.stdout = sys.stdout, StringIO()
    assert test_recursion(lambda: merge_sort(A)), \
        'Your function must be recursive'
    sys.stdout = old_stdout
