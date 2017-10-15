#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int counter = 0;
    int array[n];
    for(int i = 0; i < n; i++)
        std::cin >> array[i];
    
    for(int i = 0; i < n; i++) {
        if ((array[i] % 4 == 0) || (array[i] % 7 == 0) || (array[i] % 9 == 0))
        {
            std::cout << array[i] << std::endl;
            counter++;
            continue;
        }
        int digit = array[i] / 1000;
        if ((digit == 7) || (digit == 1) || (digit == 4) || (digit == 5) || (digit == 9) 
            || (digit == 8))
        {
            std::cout << array[i] << std::endl;
            counter++;
            continue;
        }
    }

    if (counter == 0)
        std::cout << 0 << std::endl;

return 0;
}