def solution(money, coins):
    
    if money < 0:
        return 0
    if money == 0:
        return 1
    if money > 0 and not coins:
        return 0
    
    return solution(money-coins[-1],coins) + solution(money,coins[:-1])    
# source_code переменная конец
# валидация на содержание запрещённых инструкций
exclude_patterns = ['for', 'while']
for pattern in exclude_patterns:
    reobj = re.compile(pattern)
    assert not re.findall(reobj, source_code), 'instruction "{}" could not be used'.format(pattern)
exec(source_code)  
    

if __name__ == '__main__':
    
    money = int(input())
    coinstr= input()
    if coinstr !='':
        coins = [int(x) for x in coinstr.split(" ")]
    else:
        coins = []
    true_ans = solution(money, coins)
    ans = make_exchange(money, coins)
    
    assert true_ans == ans, "False exchange!"
    
    print(ans)
