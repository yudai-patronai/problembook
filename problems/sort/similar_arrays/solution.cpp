#include <iostream>

int main() {
    int n, m;
    std::cin >> n >> m;
    int *a = new int[n];
    int *b = new int[m];
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    for (int i = 0; i < m; i++) {
        std::cin >> b[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0 ; j < n-i-1; j++) {
            if (a[j] > a[j+1]) {
                int t = a[j];
                a[j] = a[j+1];
                a[j+1] = t;
            }
        }
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0 ; j < m-i-1; j++) {
            if (b[j] > b[j+1]) {
                int t = b[j];
                b[j] = b[j+1];
                b[j+1] = t;
            }
        }
    }
    int i = 1, j = 1;
    if (a[0] != b[0]) {
        std::cout << "No\n";
        delete[] a;
        delete[] b;
        return 0;
    }
    int c = a[0];
    while (true) {
        while (i < n && a[i] == c) i++;
        while (j < m && b[j] == c) j++;
        if (i >= n || j >= m) {
            break;
        }
        if (a[i] != b[j]) {
            std::cout << "No\n";
            delete[] a;
            delete[] b;
            return 0;
        }
        c = a[i];
    }
    if (i < n || j < m) {
        std::cout << "No\n";
    } else {
        std::cout << "Yes\n";
    }
    delete[] a;
    delete[] b;
    return 0;
}
