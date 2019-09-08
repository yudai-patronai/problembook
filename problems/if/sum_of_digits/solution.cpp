#include <iostream>

int main() {
    int N;
    std::cin >> N;
    std::cout << (N % 10) + ((N / 10) % 10) + (N / 100);
    return 0;
}
