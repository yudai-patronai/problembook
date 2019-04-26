#include <iostream>
#include <cstdlib>

int main() {
    int n;
    std::cin >> n;
    int *h = new int[n];
    int *cost = new int[n];
    for (int i = 0; i < n; i++) {
        std::cin >> h[i];
        cost[i] = -1;
    }
    cost[0] = 0;
    if (n == 1) {
        std::cout << 0 << '\n';
        return 0;
    }
    cost[1] = abs(h[1] - h[0]);
    for (int i = 2; i < n; i++) {
        int from_f = abs(h[i] - h[i - 1]) + cost[i - 1];
        int from_s = 3 * abs(h[i] - h[i - 2]) + cost[i - 2];
        cost[i] = from_f < from_s ? from_f : from_s;
    }
    std::cout << cost[n - 1] << '\n';
    delete[] h;
    delete[] cost;
    return 0;
}
