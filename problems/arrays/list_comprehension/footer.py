
'''
exec(_foo)
result = list_filter(map(int, input().strip().split()))

assert not re.findall(r'append', _foo), 'append blocked'
assert not re.findall(r'extend', _foo), 'extend blocked'
assert not re.findall(r'\+', _foo), 'not bad, but blocked'
assert not re.findall(r'range', _foo), 'range blocked'
assert not re.findall(r'while', _foo), 'while blocked'
assert not re.findall(r'len', _foo), 'len blocked'

assert isinstance(list_filter([20, 5, 3]), list), 'you should return list'

print(*result)
