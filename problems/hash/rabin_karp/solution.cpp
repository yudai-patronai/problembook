#include <iostream>
#include <vector>
#include <string>
#include <cstdint>

void poly_hash(std::string const& s, std::vector<uint64_t> * h,
        std::vector<uint64_t> * p) {
    uint64_t base = 257;
    for (char c : s) {
        h->push_back(*h->rbegin() * base + static_cast<uint64_t>(c));
        p->push_back(*p->rbegin() * base);
    }
}

uint64_t poly_hash(std::string const& s) {
    uint64_t base = 257;
    uint64_t h = 0;
    for (char c : s) {
        h = h * base + static_cast<uint64_t>(c);
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
        if (s_hash == h[r] - h[l] * p[r - l]) {
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
