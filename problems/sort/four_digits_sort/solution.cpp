#include <iostream>

int main() {
    int input;
    std::cin >> input;

    int digits[4];
    for (int i = 0; i < 4; i++) {
        digits[i] = input % 10;
        input /= 10;
    }

    for (int i = 0; i < 4; i++) {
        for (int j = 2; j >= i; j--) {
            if (digits[j] > digits[j + 1]) {
                int t = digits[j];
                digits[j] = digits[j + 1];
                digits[j + 1] = t;
            }
        }
    }

    for (int i = 0; i < 4; i++) {
        if (digits[i] != 0) {
            digits[0] = digits[i];
            if (i != 0)
                digits[i] = 0;
            break;
        }
    }

    for (int i = 0; i < 4; i++)
        std::cout << digits[i];
    std::cout << std::endl;

    return 0;
}
