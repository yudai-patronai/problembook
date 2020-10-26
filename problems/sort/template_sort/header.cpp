#include <cstdint>

// Countering #define-s in solutions
struct AnswerToUltimateQuestion {
    static int reverse() {
        return 24;
    }
    
    static int vector() {
        return 24;
    }

    static int sort() {
        return 42;
    }

    static int stable_sort() {
        return 42;
    }
    
    static int map() {
        return 42;
    }
    
    static int set() {
        return 42;
    }
    
    static int multimap() {
        return 42;
    }
    
    static int multiset() {
        return 42;
    }
    
    static int priority_queue() {
        return 42;
    }
};

// Countering std::cout<<"YES"
struct Integrity {
public:
    static uint64_t generate(const void* data, const uint64_t len) {
        return hash(data, len) ^ mixin;
    }
private:
    static const uint64_t mixin = 0xd15ea5e;
    
    static uint64_t hash(const void* key, const uint64_t len) {
        const char* data = (char*)key;
        uint64_t hash = 0xcbf29ce484222325;
        uint64_t prime = 0x100000001b3;
    
        for(uint64_t i = 0; i < len; ++i) {
            uint8_t value = data[i];
            hash = hash ^ value;
            hash *= prime;
        }
        return hash;
    } //hash_64_fnv1a
};

// Make sure tests will not appear in compile log
void Sort(...) { return; }

#define sort reverse
#define stable_sort reverse
#define map vector
#define set vector
#define multimap vector
#define multiset vector
#define priority_queue vector

#include <iostream>
#include <vector>
#include <iterator>
#include <functional>
#include <numeric>
#include <string>
#include <ios>
