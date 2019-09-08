#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main() {
    std::string s;
    std::cin >> s;
    size_t n = s.size();
    std::vector<size_t> z(n, 0);
    size_t l = 0;
    size_t r = 0;
    for (size_t i = 1; i < n; ++i) {
        if (i <= r) {
            z[i] = std::min(z[i - l], r - i + 1);
        }
        while (i + z[i] < n && s[i + z[i]] == s[z[i]]) {
            ++z[i];
        }
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    for (auto v : z) {
        std::cout << v << ' ';
    }
    std::cout << '\n';
    return 0;
}
