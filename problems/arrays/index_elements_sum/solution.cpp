#include <iostream>

int main() {
    unsigned N, temp;
    unsigned answerSum = 0;
    std::cin >> N;
    for(unsigned i = 0; i < N; ++i) {
        std::cin >> temp;
        if((i % 3 == 0) && (i % 7 == 0)) {
            answerSum += temp;
        }
    }

    std::cout << answerSum << std::endl;
    return 0;
}