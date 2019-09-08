#include <iostream>
#include <string>
#include <vector>

std::vector<int> prefix_function(std::string const& s) {
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
    return pi;
}

std::vector<int> b_function(std::string const& s) {
    std::vector<int> pi = prefix_function(s);
    std::vector<int> b;
    int m = 0;
    for (int l : pi) {
        if (m >= l) {
            b.push_back(l);
        } else {
            b.push_back(pi[l - 1]);
        }
        m = m > l ? m : l;
    }
    return b;
}

int main() {
    std::string s;
    std::cin >> s;
    std::vector<int> b = b_function(s);
    for (auto v : b) {
        std::cout << v << ' ';
    }
    std::cout << '\n';
    return 0;
}
