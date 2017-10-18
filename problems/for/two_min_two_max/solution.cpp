#include <iostream>
#include <algorithm>

int main() {
    unsigned N;
    std::cin >> N;

    unsigned first, secnd;
    std::cin >> first;
    std::cin >> secnd;

    unsigned first_min = std::min(first, secnd);
    unsigned secnd_min = std::max(first, secnd);
    unsigned first_max = std::max(first, secnd);
    unsigned secnd_max = std::min(first, secnd);

    unsigned curr_num;
    for (unsigned i = 2; i < N; i++) {
        std::cin >> curr_num;

        if (curr_num >= first_max) {
            secnd_max = first_max;
            first_max = curr_num;
        } else if (curr_num >= secnd_max) {
            secnd_max = curr_num;
        } else if (curr_num <= first_min) {
            secnd_min = first_min;
            first_min = curr_num;
        } else if (curr_num <= secnd_min) {
            secnd_min = curr_num;
        }
    }

    std::cout << first_min + secnd_min  << ' ' << first_max + secnd_max << std::endl;
    return 0;
}
