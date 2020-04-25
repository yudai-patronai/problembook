#include <iostream>
#include <cmath>

bool prime_check(int32_t number) {
    if (number == 1) return false;
    if (number == 2) return true;
    if (!(number & 1)) return false;
    
    for (int32_t i = 3; i <= sqrt(number); i += 2) {
        if (number % i == 0) {
            return false;
        }
    }
    return true;
}

void permutations(int16_t number, int16_t length, int16_t current,
                  bool* used, int16_t *num_of_permutations, int32_t acc) {
    if (current == length) {
        if (prime_check(acc)) {
            ++(*num_of_permutations);
        }
    } else {
        for (int16_t variant = 0; variant < number; ++variant) {
            if (!used[variant]) {
                used[variant] = true;
                acc *= 10; acc += variant + 1;
                permutations(number, length, current + 1,
                             used, num_of_permutations, acc);
                acc /= 10;
                used[variant] = false;
            }
        }
    }
}


int main() {
    int16_t n, m;
    std::cin >> n >> m;
    bool used[10];
    for (int16_t i = 0; i < n; ++i) {
        used[i] = false;
    }
    int16_t num_of_permutations = 0;
    permutations(n, m, 0, used, &num_of_permutations, 0);
    std::cout << num_of_permutations << std::endl;
    return 0;
}
