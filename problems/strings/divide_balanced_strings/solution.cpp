#include<iostream>
#include<string>

int main() {
    std::string psp;
    int stack_depth = 0, psp_num = 0;
    std::cin >> psp;

    for (char c : psp) {
        if (c == '(') {
            stack_depth += 1;
        } else {
            stack_depth -= 1;
        }
        if (stack_depth == 0) {
            psp_num += 1;
        }
    }

    std::cout << psp_num << std::endl;
    return 0;
}
