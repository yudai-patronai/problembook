BASE = -10


def main():
    neg_decimal = int(input())
    rest = neg_decimal
    factor = 1
    result = 0

    while rest != 0:
        current_coef = rest % 10
        result += current_coef * factor

        rest //= 10
        factor *= BASE

    print(result)


if __name__ == "__main__":
    main()