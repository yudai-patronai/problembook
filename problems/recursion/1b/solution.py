def Ackermann(m,n):

    if m == 0:
        return n+1
    elif n == 0 and m > 0:
        return Ackermann(m-1, 1)
    else:
        return Ackermann(m-1, Ackermann(m, n-1))
        
        
if __name__ == '__main__':

    m = int(input())
    n = int(input())
    print(Ackermann(m,n))
