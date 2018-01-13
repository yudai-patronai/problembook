#include <iostream>
#include <string>

using std::string;

int main() {
    string input;
    input.resize(256);
    std::getline(std::cin, input);
    string reversed(input.rbegin(), input.rend());
    std::cout << reversed << std::endl;

    return 0;
}
