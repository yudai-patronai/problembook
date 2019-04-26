#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

int main() {
    std::string s;
    std::getline(std::cin, s);
    size_t n = s.size();
    size_t l = 0;
    size_t r = 0;
    std::vector<size_t> p(n, 0);
    for (size_t i = 0; i < n; ++i) {
        size_t k = i > r ? 0 : std::min(r - i, p[l + r - i]);
        while (k < i && i + k + 1 < n && s[i - k - 1] == s[i + k + 1]) {
            ++k;
        }
        if (i + k > r) {
            l = i - k;
            r = i + k;
        }
        p[i] = k;
    }
    for (size_t v : p) {
        std::cout << v * 2 + 1 << ' ';
    }
    std::cout << '\n';
    return 0;
}
