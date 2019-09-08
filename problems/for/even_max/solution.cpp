#include <iostream>

int main() {
    int emax = 0;
    int num;
    std::cin >> num;
    while (num != 0) {
        if (num % 2 == 0 && num > emax) {
            emax = num;
        }
        std::cin >> num;
    }
    std::cout << emax << "\n";
    return 0;
}
