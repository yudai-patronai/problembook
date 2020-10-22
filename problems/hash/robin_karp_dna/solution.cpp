#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <math.h>

using std::vector;
using std::map;
using std::string;
using std::set;
vector<string> findRepDna(string &s) {
    map<char, int> DNA{{'A', 0},
    {'C', 1},
    {'G', 2},
    {'T', 3}};
    vector<int> numbers;
    int n = s.length();
    for (size_t i = 0; i < s.length(); i++) {
        numbers.push_back(DNA[s[i]]);
    }
    set<int> seen;
    set <string> out;
    int L = 10;
    if (n < L)
        return vector<string>();

    int a = 4, aL = (1 << (2 * L)) - 1;
    int hash = 0;

    for (int i = 0; i < L; i++) hash = hash * a + numbers[i];
    for (int start = 0; start < n - L + 1; start++) {
        if (start != 0)
            hash = (hash * a + numbers[start + L - 1]) & aL;

        if (seen.find(hash) != seen.end())
            out.insert(s.substr(start, L));
        seen.insert(hash);
    }
    vector <string> out_v(out.begin(), out.end());
    return out_v;
}
int main() {
    std::vector<std::string> dna_substr;
    std::string dna_str;
    getline(std::cin, dna_str);
    dna_substr = findRepDna(dna_str);
    for (size_t i = 0; i < dna_substr.size(); i++) {
        std:: cout << dna_substr[i] <<" ";
    }
    return 0;
}
