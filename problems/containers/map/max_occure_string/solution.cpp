#include <iostream>
#include <map>
#include <algorithm>
#include <string>

int main() {
    int n;
    std::cin >> n;
    std::map<std::string, int> hist;

    std::string word;
    for (int i = 0; i < n; i++) {
        std::cin >> word;
        std::transform(word.begin(), word.end(), word.begin(), ::tolower);

        if (hist.count(word) == 0)
            hist[word] = 0;

        hist[word] += 1;
    }

    auto most_popular = std::max_element
    (
        std::begin(hist), std::end(hist),
        [] (const std::pair<std::string, int>& p1,
            const std::pair<std::string, int>& p2) {
            return p1.second < p2.second;
        });
    std::cout << most_popular->first
              << ' '
              << most_popular->second
              << std::endl;

    return 0;
}
