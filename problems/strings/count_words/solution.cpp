#include <iostream>

int main() {
    unsigned count = 0;
    std::string tmp;

    while (std::cin >> tmp) {
        ++count;
    }

    std::cout << count << std::endl;

    return 0;
}
