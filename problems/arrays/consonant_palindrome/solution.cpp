#include <string>
#include <vector>
#include <iostream>
#include <cstdint>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;

int main() {
    string s;
    string vowels = "aeiouy";

    cin >> s;

    int l = s.length();

    vector<int> consonants;

    for (int i = 0; i < l; i++) {
        char c = s[i];
        if (vowels.find(c) == string::npos) {
            consonants.push_back(i);
        }
    }

    uint64_t cs = consonants.size();
    for (uint64_t i = 0; i < cs / 2; i++) {
        if (s[consonants[i]] != s[consonants[cs - i - 1]]) {
            cout << "NO" << endl;

            return 0;
        }
    }

    cout << "YES" << endl;

    return 0;
}
