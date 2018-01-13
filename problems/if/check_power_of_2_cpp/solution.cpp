#include <iostream>

int main() {
    uint64_t n;
    std::cin >> n;

    if ((n & (n - 1)) == 0)
        std::cout << "YES";
    else
        std::cout << "NO";

    return 0;
}
