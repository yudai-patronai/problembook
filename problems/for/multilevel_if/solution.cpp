#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int *array = new int[n];
    int counter = 0;
    for (int i = 0; i < n; i++)
        std::cin >> array[i];

    for (int i = 0; i < n; i++) {
        int digit = array[i] / 1000;
        if ((array[i] % 4 == 0) && ((digit != 4 && digit != 5))) {
            std::cout << array[i] << std::endl;
            counter++;
            continue;
        }
        if ((array[i] % 7 == 0) && ((digit != 7 && digit != 1))) {
            std::cout << array[i] << std::endl;
            counter++;
            continue;
        }
        if ((array[i] % 9 == 0) && ((digit != 9 && digit != 8))) {
            std::cout << array[i] << std::endl;
            counter++;
            continue;
        }
    }

    if (counter == 0)
        std::cout << 0 << std::endl;

    delete[] array;
    return 0;
}
