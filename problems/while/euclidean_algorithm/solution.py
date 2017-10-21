a = int(input())
b = int(input())


def eucl_alg(firstNumber, secondNumber):
    while firstNumber != secondNumber:
        if firstNumber > secondNumber:
            firstNumber -= secondNumber
        else:
            secondNumber -= firstNumber

    return firstNumber

print(eucl_alg(a, b))
