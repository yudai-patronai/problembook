#'''  # source_code переменная конец

# Валидация на содержание запрещённых инструкций
exclude_patterns = ['for', 'while']

for pattern in exclude_patterns:
    reobj = re.compile(pattern)
    assert not re.findall(reobj, source_code), \
        'instruction "{}" could not be used'.format(pattern)

# Считывание происходит здесь, в footer-е.
# Считанная строка затем в потоковом виде подаётся в функцию solution-а.
# Временное перенаправление ввода-вывода и считывание входных данных
# в основной код необходимо, потому что входные данные используются
# при проверке на рекурсию.
x1, y1, x2, y2 = (int(input()) for _ in range(4))
input_str = '\n'.join(map(str, (x1, y1, x2, y2)))

# Временное перенаправление ввода-вывода
old_stdout, old_stdin = sys.stdout, sys.stdin
sys.stdout = StringIO()
sys.stdin = StringIO(input_str)

exec(source_code)
# Сохранение вывода solution-а, чтобы последующий возможный вывод
# проверки на рекурсию выводил в тот же поток.
print_val = sys.stdout.getvalue()

# Для нового запуска в процесе проверки на рекурсию нужны новые потоки.
sys.stdout = StringIO()
sys.stdin = StringIO(input_str)
assert (x1, y1) == (x2, y2) or test_recursion(lambda: exec(source_code))

# Возврат значений потокам ввода-вывода.
sys.stdout, sys.stdin = old_stdout, old_stdin

print(print_val, end='')
