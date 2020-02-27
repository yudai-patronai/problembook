#include <iostream>

int main() {
    unsigned N;
    std::cin >> N;
    unsigned min = UINT32_MAX;
    unsigned max = 0;
    for (unsigned i = 0; i < N; ++i) {
        int tmp;
        std::cin >> tmp;
        if (tmp < min) {
            min = tmp;
        }
        if (tmp > max) {
            max = tmp;
        }
    }
    std::cout << max - min - N + 1 << std::endl;
    return 0;
}
