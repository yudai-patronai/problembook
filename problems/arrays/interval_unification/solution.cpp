#include<iostream>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, curr_a, curr_b;
    std::cin >> n;
    
    std::cin >> curr_a >> curr_b;
    for (int i = 1; i < n; ++i) {
        int temp_a, temp_b;
        std::cin >> temp_a >> temp_b;
        if (temp_a <= curr_b) {
            curr_b = temp_b > curr_b ? temp_b : curr_b;
        } else {
            std::cout << curr_a << ' ' << curr_b << std::endl;
            curr_a = temp_a;
            curr_b = temp_b;
        }
    }
    std::cout << curr_a << ' ' << curr_b << std::endl;
    
    return 0;
}
