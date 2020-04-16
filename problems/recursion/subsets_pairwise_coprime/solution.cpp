#include <iostream> 
#include <vector>

uint64_t gcd(uint64_t a, uint64_t b) {
    while (b) {
        a %= b;
        a = a ^ b;
        b = a ^ b;
        a = a ^ b;
    }
    return a;
}

int main() {
    uint16_t N;
    std::cin >> N;
    
    std::vector<uint64_t> numbers;
    numbers.reserve(N);
    
    uint64_t temp;
    
    for (uint16_t i = 0; i < N; ++i) {
        std::cin >> temp;
        numbers.push_back(temp);
    }
    
    std::vector<uint64_t> masks;
    masks.reserve(N);
    
    for (uint16_t i = 0; i < N; ++i) {
        temp = 0;
        for (uint16_t j = 0; j < N; ++j) {
            if (gcd(numbers[i], numbers[j]) > 1) {
                temp |= (1 << j);
            }
        }
        
        temp =  temp & (~(1 << i));
        masks.push_back(temp);
    }
    
    uint64_t count = 0;
    
    for (uint64_t cur_set = 0; cur_set < (1ull << N); ++cur_set) {
        bool good = true;
        for (uint16_t i = 0; i < N; ++i) {
            if ((cur_set & (1 << i)) && (cur_set & masks[i])) {
                good = false;
                break;
            }
        }
        if (good) {
            ++count;
        }
    }
    
    std::cout << count << "\n";
}
