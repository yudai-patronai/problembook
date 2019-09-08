#include <iostream>
#include <string>

int main() {
    std::string input1, input2;
    getline(std::cin, input1);
    getline(std::cin, input2);
    input1 += input1;
    std::string::size_type answer = 0;
    if (std::string::npos != (answer = input1.find(input2, answer))) {
        std::cout << answer << '\n';
    } else {
        std::cout << -1 << '\n';
    }
    return 0;
}
