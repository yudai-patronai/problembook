#include <iostream>
#include <set>

int main() {
    int n;
    std::cin >> n;
    std::set<int> result;
    for (int i = 0; i < n; ++i) {
        int input;
        std::cin >> input;
        result.insert(input);
    }

    std::cout << result.size() << std::endl;
    return 0;
}
