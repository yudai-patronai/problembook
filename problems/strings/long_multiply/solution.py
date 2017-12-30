def mul(num_1, num_2, base):

    ans_list = []
    for i in range(len(num_2)):
        ans = ''
        in_mind = 0
        for j in range(len(num_1)):
            digit_mul = int(num_2[-i-1]) * int(num_1[-j-1])
            ans += str((digit_mul + in_mind) % base)
            in_mind = (digit_mul + in_mind) // base

        if in_mind != 0:
            ans += str(in_mind)        

        ans_list.append(ans[::-1])
        
    for i in range(len(ans_list)):
        ans_list[i] += '0' * i
    
    for i in range(len(ans_list)):
        ans_list[i] = '0' * (len(ans_list[-1]) - len(ans_list[i])) + ans_list[i]
    
    in_mind = 0
    ans = ''
    for i in range(len(ans_list[-1])):
        sum_ = 0
        for num in ans_list:
            sum_ += int(num[-i-1])
        ans += str((sum_ + in_mind) % base)
        in_mind = (sum_ + in_mind) // base
    
    if in_mind != 0:
        ans += str(in_mind)
       
    return ans[::-1]


if __name__ == '__main__':

    base = int(input())
    num_1 = input()
    num_2 = input()
    
    print(mul(num_1, num_2, base))


