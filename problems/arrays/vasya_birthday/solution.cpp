#include <iostream>

int main() {
    unsigned N;
    unsigned answer = 0;
    std::cin >> N;
    unsigned array[N];
    for (unsigned i = 0; i < N; ++i) {
        std::cin >> array[i];
    }

    // bubble sort
    for (unsigned i = 0; i < N; ++i) {
        for (unsigned j = 1; j < N; ++j) {
            if (array[j] < array[j - 1]) {
                unsigned temp = array[j];
                array[j] = array[j - 1];
                array[j - 1] = temp;
            }
        }
    }

    for (unsigned i = 0; i < N; ++i) {
        if (array[i + 1] != (array[i] + 1))
            answer += statues[i + 1] - statues[i] - 1;
    }

    std::cout << answer << std::endl;

    return 0;
}
