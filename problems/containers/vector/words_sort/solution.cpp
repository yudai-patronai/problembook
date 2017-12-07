#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

int main() {
    int n;
    std::cin >> n;
    std::vector<std::string> words;

    for (int i = 0; i < n; i++) {
        std::string word;
        std::cin >> word;
        std::transform(word.begin(), word.end(), word.begin(), ::tolower);
        words.push_back(word);
    }

    std::sort(words.rbegin(), words.rend());

    int last_same = 0;
    std::cout << words[0];
    for (int i = 1; i < n; i++) {
        if (words[i] != words[last_same]) {
            last_same = i;
            std::cout << ' ' << words[i];
        }
    }
    std::cout << std::endl;

    return 0;
}
