#include <iostream>
#include <string>

bool check(std::string const& s, std::string const& t, std::string const& u) {
    if (t == u && t == "") {
        return true;
    }
    bool result = false;
    if (t != "" && s[0] == t[0]) {
        result |= check(s.substr(1), t.substr(1), u);
    }
    if (!result && u != "" && s[0] == u[0]) {
        result |= check(s.substr(1), t, u.substr(1));
    }
    return result;
}

int main() {
    std::string s, t, u;
    std::getline(std::cin, s);
    std::getline(std::cin, t);
    std::getline(std::cin, u);
    size_t n = s.size();
    size_t m = t.size();
    size_t k = u.size();
    for (size_t i = 0; i < n; ++i) {
        if (check(s.substr(i, m + k), t, u)) {
            std::cout << "Yes\n";
            return 0;
        }
    }
    std::cout << "No\n";
    return 0;
}
