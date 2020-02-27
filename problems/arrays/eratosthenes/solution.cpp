#include <iostream>

int main() {
    int n;
    std::cin >> n;
    n++;
    int flag[n];
    for (int i = 0; i < n; i++) {
        flag[i] = 1;
    }
    for (int i = 2; i < n; i++) {
        if (flag[i] == 0) {
            continue;
        }
        for (int j = i + i; j < n; j += i) {
            flag[j] = 0;
        }
    }
    for (int i = 2; i < n; i++) {
        if (flag[i] != 0) {
            std::cout << i << ' ';
        }
    }
    return 0;
}