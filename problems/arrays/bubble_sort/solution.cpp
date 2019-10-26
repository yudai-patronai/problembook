#include <iostream>

int main() {
    unsigned N, temp;
    std::cin >> N;
    int a[N];
    for (unsigned i = 0; i < N; ++i) {
        std::cin >> a[i];
    }

    for (unsigned i = 0; i < (N - 1); ++i) {
        for (unsigned j = 0; j < (N - i - 1); ++j) {
            if (a[j] > a[j + 1]) {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }

    for (unsigned i = 0; i < N; ++i) {
        std::cout << a[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
