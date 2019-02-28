#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


std::vector<size_t> z_func(std::string const& s) {
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
    return z;
}

int main() {
    std::string s;
    std::cin >> s;
    std::string t;
    t.resize(s.size());
    std::reverse_copy(s.begin(), s.end(), t.begin());
    s += "#" + t;
    std::vector<size_t> a = z_func(s);
    for (size_t i = 1; i <= t.size(); ++i) {
        std::cout << *(a.end() - i) << ' ';
    }
    std::cout << '\n';
    return 0;
}
