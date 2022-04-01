#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>

uint32_t get_results_raw_sin(uint32_t min, uint32_t max, uint32_t min_channel, uint32_t max_channel, uint32_t zero, uint32_t channel);
uint32_t get_results_raw_linear(uint32_t min, uint32_t max, uint32_t min_channel, uint32_t max_channel, uint32_t zero, uint32_t channel);


struct Tester {
    uint32_t min, max, zero;
    uint32_t min_channel, max_channel;

    uint32_t type;

    uint32_t operator()(uint32_t channel) {
        switch (type) {
            case 167:
            case 172:
            case 91:
                return get_results_raw_sin(min, max, min_channel, max_channel, zero, channel);
                break;
            case 218:
            case 429:
            case 625:
                return get_results_raw_linear(min, max, min_channel, max_channel, zero, channel);
                break;
            default:
                std::cout << "Bad tester type!\n";
                std::exit(2);
                break;
        }
    }
};

Tester gt;

unsigned int get_results(unsigned int channel) {
    static unsigned int calls = 0;

    calls++;
    if (calls > 25) {
        std::cout << "Too many calls!\n";
        std::exit(3);
        return static_cast<uint32_t>(-1);
    }

    return gt(channel);
}

void detect();
