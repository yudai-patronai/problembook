#include <string>
#include <regex>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <vector>


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

