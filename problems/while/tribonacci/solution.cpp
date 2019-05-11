#include <iostream>

int main() {
    int  N, a, b, c, d, number;
    a = 0; b = 0; c = 1;
    std::cin >> N;
    if (N < 0) {
        std::cout << 0;
        return 0;
    }
    if (N == 0) {
        std::cout << 2;
        return 0;
    }
    number = 2;
    while (c <= N) {
        d = a + b + c;
        a = b;  b = c; c = d;
        number++;
    }
    std::cout << number;
    return 0;
}
