#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int *a = new int[n];
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int mind = n;
    for (int i = 0; i < n; i++) {
        if (a[i] < 0) {
            for (int j = i+1; j < std::min(n, i+mind); j++) {
                if (a[i] + a[j] == 0) {
                    mind = j - i;
                }
            }
        }
    }
    if (mind == n) {
        std::cout << 0 << '\n';
    } else {
        std::cout << mind << '\n';
    }
    delete[] a;
    return 0;
}
