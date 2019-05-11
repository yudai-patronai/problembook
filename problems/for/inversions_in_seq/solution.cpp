#include <iostream>

int main() {
    int counts = 0;
    int  N, M;
    std::cin >> N;
    while (N != 0) {
        std::cin >> M;
        if (N < M) counts++;
        N = M;
    }
    std::cout << counts;
    return 0;
}
