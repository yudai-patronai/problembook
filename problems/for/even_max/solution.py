if __name__ == "__main__":
    emax = 0
    num = int(input())
    while num != 0:
        if not num % 2 and num > emax:
            emax = num
        num = int(input())
    print(emax)
