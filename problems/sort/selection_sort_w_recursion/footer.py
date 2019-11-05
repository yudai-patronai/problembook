#'''  # source_code переменная конец

# валидация на содержание запрещённых инструкций
exclude_patterns = [r'\s*\.\s*sort', r'sorted']
for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), \
        'You are using restricted constructions'

# Считывание происходит здесь, в footer-е.
# Считанная строка затем в потоковом виде подаётся в функцию solution-а.
# Временное перенаправление ввода-вывода и считывание входных данных
# в основной код необходимо, потому что входные данные используются
# при проверке на рекурсию.
input_str = input()
array = list(map(int, input_str.split()))

# Временное перенаправление ввода-вывода
old_stdout, old_stdin = sys.stdout, sys.stdin
sys.stdin, sys.stdout = StringIO(input_str), StringIO()

exec(source_code)
# Сохранение вывода solution-а, чтобы последующий возможный вывод
# проверки на рекурсию выводил в тот же поток.
print_val = sys.stdout.getvalue()

# Для нового запуска в процесе проверки на рекурсию нужны новые потоки.
sys.stdin, sys.stdout = StringIO(input_str), StringIO()
assert len(array) <= 1 or test_recursion(lambda: exec(source_code))

# Возврат значений потокам ввода-вывода.
sys.stdout, sys.stdin = old_stdout, old_stdin

print(print_val, end='')
