#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int *a = new int[n];
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int *b = new int[n];
    for (int i = 0; i < n; i++) {
        std::cin >> b[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j+1] || (a[j] == a[j+1] && b[j] > b[j+1])) {
                int t = a[j];
                a[j] = a[j+1];
                a[j+1] = t;
                t = b[j];
                b[j] = b[j+1];
                b[j+1] = t;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        std::cout << a[i] << ' ';
    }
    std::cout << '\n';
    for (int i = 0; i < n; i++) {
        std::cout << b[i] << ' ';
    }
    delete[] a;
    delete[] b;
    return 0;
}
