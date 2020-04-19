#include <iostream>
#include <cmath>

bool prime_check(int32_t number) {
    if (number == 1) return false;
    for (int32_t i = 2; i <= sqrt(number); ++i)
        if (number % i == 0)
        return false;
    return true;
}

void permutations(int16_t number, int16_t length, int16_t current,
                  int16_t* buffer, bool* used, int16_t *num_of_permutations) {
    if (current == length) {
        int32_t tmp = 0;
        for (int16_t i = 0; i < length; ++i)
            tmp += buffer[i] * pow(10, length - i - 1);
        if (prime_check(tmp))
            ++(*num_of_permutations);
    } else {
        for (int16_t variant = 0; variant < number; ++variant) {
            if (!used[variant]) {
                buffer[current] = variant + 1;
                used[variant] = true;
                permutations(number, length, current + 1,
                             buffer, used, num_of_permutations);
                used[variant] = false;
            }
        }
    }
}


int main() {
    int16_t n, m;
    std::cin >> n >> m;
    int16_t* buffer = new int16_t[m];
    bool* used = new bool[n];
    for (int16_t i = 0; i < n; ++i)
        used[i] = false;
    int16_t num_of_permutations = 0;
    permutations(n, m, 0, buffer, used, &num_of_permutations);
    std::cout << num_of_permutations << std::endl;
    delete[] buffer;
    delete[] used;
    return 0;
}

