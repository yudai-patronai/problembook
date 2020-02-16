#include <iostream>
#include <vector>
#include <string>
#include <cstdint>

const uint64_t M = (1UL << 32) - 5UL;
const uint64_t B = 239UL;

void poly_hash(std::string const& s, std::vector<uint64_t> * h,
        std::vector<uint64_t> * p) {
    for (char c : s) {
        h->push_back(((*h->rbegin() * B) % M +
                     static_cast<uint64_t>(c - 'a' + 1)) % M);
        p->push_back((*p->rbegin() * B) % M);
    }
}

uint64_t poly_hash(std::string const& s) {
    uint64_t h = 0;
    for (char c : s) {
        h = ((h * B) % M + static_cast<uint64_t>(c - 'a' + 1)) % M;
    }
    return h;
}

int main() {
    std::string s, t;
    std::getline(std::cin, s);
    std::getline(std::cin, t);
    uint64_t s_hash = poly_hash(s);
    std::vector<uint64_t> h = {0};
    std::vector<uint64_t> p = {1};
    poly_hash(t, &h, &p);
    size_t n = t.size() - s.size() + 1;
    bool flag = false;
    for (size_t l = 0; l < n; ++l) {
        size_t r = l + s.size();
        if (s_hash == (h[r] + M - (h[l] * p[r - l]) % M) % M) {
            std::cout << l << ' ';
            flag = true;
        }
    }
    if (!flag) {
        std::cout << -1;
    }
    std::cout << '\n';
    return 0;
}
