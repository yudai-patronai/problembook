#''' # source_code переменная конец

# валидация на содержание запрещённых инструкций
exclude_patterns = [r'for([^a-zA-Z_0-9]|$)', r'while']

for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), \
        'instruction "{}" could not be used'.format(reobj)


exec(source_code)
