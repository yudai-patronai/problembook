#include <iostream>

int main() {
    int n, k;
    std::cin >> n >> k;
    int *a = new int[n];
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int *b = new int[n];
    for (int j = 0; j < k; j++) {
        for (int i = 0; i < n; i++) {
            b[i] = static_cast<int>((a[(i - 1 + n) % n] + a[i]
                                     + a[(i + 1) % n]) / 3.0);
        }
        for (int i = 0; i < n; i++) {
            a[i] = b[i];
        }
    }
    for (int i = 0; i < n; i++) {
        std::cout << a[i] << ' ';
    }
    delete[] a;
    delete[] b;
    return 0;
}
