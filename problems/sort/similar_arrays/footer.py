#'''  # source_code переменная конец

# валидация на содержание запрещённых инструкций
exclude_patterns = [r'\s*\.\s*sort', r'sorted', r'set']
for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), \
        'You are using restricted constructions'

exec(source_code)
