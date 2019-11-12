#'''  # source_code переменная конец

# Валидация на содержание запрещённых инструкций
exclude_patterns = [r'for([^a-zA-Z_0-9]|$)', r'while']

for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), \
        'instruction "{}" could not be used'.format(reobj)

exec(source_code)  # объект is_add_35 становится доступным

sys.setrecursionlimit(10003)  # позволяет запускать функцию от n <= 30000

n = int(input())

# Проверка на рекурсивный вызов, если n достаточно большое
assert n <= 6 or n % 3 == 1 or n % 5 == 1 or \
    test_recursion(lambda: is_add_35(n)), \
    'Function is_add_35 must be recursive'

print('YES' if is_add_35(n) else 'NO')
