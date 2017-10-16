#include <iostream>

int main() {
    const unsigned long int size = 2000000;
    unsigned int array[size];
    unsigned int n, number;
    std::cin >> n;
    std::cin >> number;
    for (unsigned int i = 0; i < n; i++)
        std::cin >> array[i];
    unsigned int left = 0;
    unsigned int right = n - 1;
    while (left <= right) {
        unsigned int middle = (left + right) / 2;
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
