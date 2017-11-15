def make_exchange(money, coins):
    
    if money < 0:
        return 0
    if money == 0:
        return 1
    if money > 0 and not coins:
        return 0
    
    return make_exchange(money-coins[-1],coins) + make_exchange(money,coins[:-1])
    

money, coins = 20, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(make_exchange(money, coins))
