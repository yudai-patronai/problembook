
#''' #  ЭТО не комментарий, а конец переменной source_code из header

#  валидация на содержание запрещённых инструкций
exclude_patterns = [r'.*\s*\.\s*sort\s*\(', r'.*sorted\s*\(']

count = 0
for reobj in exclude_patterns:
    for restricted_match in re.findall(reobj, source_code):
        count += 1
        print('[FORBIDDEN]', restricted_match)

if count:
    raise AssertionError('You are using forbidden constructions. They are listed above.')

exec(source_code)
