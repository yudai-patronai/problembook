#'''# source_code переменная конец
# валидация на содержание запрещённых инструкций
exclude_patterns = [r'for([^a-zA-Z_0-9]|$)', r'while']
for reobj in exclude_patterns:
    assert not re.findall(reobj, source_code), \
    	'instruction "{}" could not be used'.format(pattern)
exec(source_code)  
    
money = int(input())
coinstr = input()
if coinstr !='':
    coins = [int(x) for x in coinstr.split(" ")]
else:
    coins = []
ans = make_exchange(money, coins)
print(ans)
