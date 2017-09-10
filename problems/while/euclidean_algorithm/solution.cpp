#include <iostream>

int main()
{
  int firstNumber = 0;
  int secondNumber = 0;

  std::cin >> firstNumber >> secondNumber;

  int temp = 0;
  while (secondNumber != 0)
  {
    temp = secondNumber;
    secondNumber = firstNumber % secondNumber;
    firstNumber = temp;
  }

  std::cout << firstNumber << std::endl;

  return 0;
}
