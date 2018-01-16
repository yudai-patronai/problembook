#include <ctype.h>
#include <iostream>
#include <string>

int main() {
    std::string in;
    std::getline(std::cin, in);

    int number = 0;
    int temp = 0;
    std::string num;
    for (int i = 0; i < in.size(); ++i) {
        if (isdigit(in.at(i)))
            num += in.at(i);
        else
            num.erase();
        temp = atoi(num.c_str());
        if (temp > number)
            number = temp;
    }

    std::cout << number << std::endl;
    return 0;
}
