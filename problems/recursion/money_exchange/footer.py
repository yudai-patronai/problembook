def solution(money, coins):
    
    if money < 0:
        return 0
    if money == 0:
        return 1
    if money > 0 and not coins:
        return 0
    
    return solution(money-coins[-1],coins) + solution(money,coins[:-1])    
    

if __name__ == '__main__':
    
    money = int(input())
    coins = [int(x) for x in input().split(" ")]
    
    true_ans = solution(money, coins)
    ans = make_exchange(money, coins)
    
    assert true_ans == ans, "False exchange!"
    
    print(ans)
