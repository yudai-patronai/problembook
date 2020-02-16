#'''  # source_code переменная конец

# Валидация на содержание запрещённых инструкций
exclude_patterns = [r'for([^a-zA-Z_0-9]|$)', r'while']

for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), \
        'instruction "{}" could not be used'.format(reobj)

# Считывание происходит здесь, в footer-е.
# Считанная строка затем в потоковом виде подаётся в функцию solution-а.
# Временное перенаправление ввода-вывода и считывание входных данных
# в основной код необходимо, потому что входные данные используются
# при проверке на рекурсию.
nums = list(map(int, input().split()))
num_exact = int(input())
input_str = '{}\n{}'.format(' '.join(map(str, nums)), num_exact)

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
assert len(nums) <= 3 or num_exact in nums[len(nums) // 2: len(nums) // 2 + 2]\
    or test_recursion(lambda: exec(source_code))

# Возврат значений потокам ввода-вывода.
sys.stdout, sys.stdin = old_stdout, old_stdin

print(print_val, end='')
