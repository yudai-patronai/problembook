/*
на стандартном потоке ввода задаются два целых числа, не меньшие -32000 и не большие 32000.
На стандартный поток вывода напечатайте сумму этих чисел.
*/
#include <iostream>

int main()
{
  int firstNumber = 0;
  int secondNumber = 0;

  std::cin >> firstNumber;
  std::cin >> secondNumber;

  std::cout << firstNumber + secondNumber << std::endl;

  return 0;
}
