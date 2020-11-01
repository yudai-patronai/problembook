def make_exchange(money, coins):
    if money < 0:
        return 0
    if money == 0:
        return 1
    if money > 0 and not coins:
        return 0

    return make_exchange(money-coins[-1],coins) +\
        make_exchange(money,coins[:-1])

