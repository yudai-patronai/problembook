#include <iostream>
#include <map>

int main() {
    int n;
    std::cin >> n;
    std::map<int, int> stones;
    int count = 0;
    for (int i = 0; i < n; ++i) {
        int c;
        std::cin >> c;
        stones[c] += 1;
        if (stones[c] == 3) {
            std::cout << 0 << '\n';
            return 0;
        }
        if (stones[c] == 2) {
            ++count;
            if (count == 2) {
                std::cout << 0 << '\n';
                return 0;
            }
        }
    }
    std::cout << 1 << '\n';
    return 0;
}
