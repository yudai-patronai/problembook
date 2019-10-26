#include <iostream>

int main() {
  int firstNumber = 0;
  int secondNumber = 0;

  std::cin >> firstNumber >> secondNumber;

  if (firstNumber > secondNumber)
    std::cout << 1 << std::endl;
  else if (firstNumber < secondNumber)
    std::cout << 2 << std::endl;
  else
    std::cout << 0 << std::endl;

  return 0;
}
