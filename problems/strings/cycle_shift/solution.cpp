#include <iostream>
#include <string>

int main() {
    std::string input1, input2;
    getline(std::cin, input1);
    getline(std::cin, input2);
    input1 += input1;
    std::string::size_type answer = 0;
    while(std::string::npos != (answer = input1.find(input2, answer)))
    {
        cout << answer << endl;
        return 0;
    }
    cout << -1 << endl;
    return 0;
}