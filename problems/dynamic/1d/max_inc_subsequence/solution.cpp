#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int* arr = new int[n];
    for (int i = 0; i < n; i++)
        std::cin >> arr[i];

    int* d = new int[n];
    for (int i = 0; i < n; i++) {
        d[i] = 1;
        for (int j = 0; j < i; j++)
            if (arr[j] < arr[i])
                d[i] = std::max(d[i], 1 + d[j]);
    }

    int ans = d[0];
    for (int i = 0; i < n; i++)
        ans = std::max(ans, d[i]);

    delete[] d;
    delete[] arr;

    std::cout << ans << std::endl;
}
