#include <iostream>
#include <string>

int main() {
    std::string input;
    input.resize(256);
    std::getline(std::cin, input);
    std::string output = "";
    output.resize(input.size());
    for(unsigned i = 0; i < input.size(); i++) {
        if((i % 5 == 0) && (i != 0)) {
            output.append(" ");
        }
        output += input.at(i);
    }
    std::cout << output << std::endl;
    return 0;
}