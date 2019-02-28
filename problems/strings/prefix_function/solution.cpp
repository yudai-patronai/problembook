#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string s;
    std::cin >> s;
    size_t n = s.size();
    std::vector<int> pi(n, 0);
    for (size_t i = 1; i < n; ++i) {
        size_t j = pi[i - 1];
        while (j > 0 && s[j] != s[i]) {
            j = pi[j - 1];
        }
        if (s[i] == s[j]) {
            ++j;
        }
        pi[i] = j;
    }
    for (auto v : pi) {
        std::cout << v << ' ';
    }
    std::cout << '\n';
    return 0;
}
