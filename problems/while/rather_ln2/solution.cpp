#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int t = 1;
    int k = 0;
    while (t < n) {
        t *= 2;
        ++k;
    }
    std::cout << k << '\n';
    return 0;
}
