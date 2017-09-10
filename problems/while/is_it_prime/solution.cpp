#include <iostream>
#include <math.h>

int main()
{
  int input = 0;

  std::cin >> input;

  for (int i = 2; i <= sqrt(input); ++i)
  {
    if (input % i == 0)
    {
      std::cout << 0 << std::endl;
      return 0;
    }
  }

  std::cout << 1 << std::endl;

  return 0;
}
