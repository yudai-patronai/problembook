#include <iostream>

int main() {
    double a;
    double p[] = {1.0, 1.0, 1.0, 0.75, 0.5, 0.0};
    for (int i = 0; i < 6; ++i) {
        int k;
        std::cin >> k;
        a += k * p[i];
    }
    std::cout << a << '\n';
    return 0;
}
