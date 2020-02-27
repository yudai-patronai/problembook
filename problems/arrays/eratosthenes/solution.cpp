#include <iostream>

int main() {
    int n;
    std::cin >> n;
    n++;
    int arr[n];
    for (int i = 0; i < n; i++) {
        arr[i] = i;
    }
    for (int i = 2; i < n; i++) {
        if (arr[i] == 0) {
            continue;
        }
        for (int j = i + i; j < n; j += i) {
            arr[j] = 0;
        }
    }
    for (int i = 2; i < n; i++) {
        if (arr[i] != 0) {
            std::cout << i << ' ';
        }
    }
    return 0;
}