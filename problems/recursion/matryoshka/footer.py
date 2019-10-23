'''

exclude_patterns = ['for', 'while']

for pattern in exclude_patterns:
    reobj = re.compile(pattern)
    assert not re.findall(reobj, source_code) '{} could not be used'.format(pattern)

exec(source_code)
