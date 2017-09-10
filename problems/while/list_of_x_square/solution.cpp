#include <iostream>

int main()
{
  int inputNumber = 0;

  std::cin >> inputNumber;

  int square = 1;
  while (square * square <= inputNumber)
  {
    std::cout << square * square << " ";
    square++;
  }

  std::cout << std::endl;

  return 0;
}
