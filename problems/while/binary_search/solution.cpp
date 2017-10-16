#include <iostream>

int main() {
    const int size = 1000000;
    int array[1000000];
    int n, number;
    std::cin >> n;
    std::cin >> number;
    for(int i = 0; i < n; i++)
        std::cin >> array[i];
    int left = 0;
    int right = n - 1;
    while (left <= right) {
        int middle = (left + right) / 2;
        if (array[middle] == number) {
            std::cout << middle + 1 << std::endl;
            return 0;
        }
        else if (array[middle] > number)
            right = middle - 1;
        else
            left = middle + 1;
    }
    std::cout << -1 << std::endl;
    return 0;
}
