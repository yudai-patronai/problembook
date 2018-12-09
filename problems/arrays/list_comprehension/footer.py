
'''
exec(_foo)
result = list_filter(map(int, input().strip().split()))

assert not re.findall(r'append', _foo), 'append запрещен'
assert not re.findall(r'extend', _foo), 'extend запрещен'
assert not re.findall(r'+', _foo), 'not bad, но не прокатит')
assert isinstance(list_filter([20, 5, 3]), list), 'надо вернуть list'

print(*result)
