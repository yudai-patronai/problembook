def min_from_digsum_digs(sum_dig, num_digs):
    if num_digs * 9 < sum_dig or num_digs > sum_dig:
        return None

    num = 0

    for i in range(num_digs):
        rest_digs = num_digs - i

        if sum_dig - 9 > rest_digs:
            dig_incr = 9
        else:
            dig_incr = sum_dig - rest_digs + 1

        num += dig_incr * 10**i
        sum_dig -= dig_incr

    return num


s, n = input().split()
s, n = int(s), int(n)

res = min_from_digsum_digs(s, n)

if res is None:
    print('impossible')
else:
    print(res)
