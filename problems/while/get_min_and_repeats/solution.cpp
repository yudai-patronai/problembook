#include <iostream>

int main()
{
  int n = 0;
  int min = 10000;
  int repeatCounter = 1;

  std::cin >> n;

  for(int i = 0; i < n; ++i)
  {
    int input;
    std::cin >> input;

    if (min == input)
      repeatCounter++;
    else if (min > input)
    {
      min = input;
      repeatCounter = 1;
    }
  }

  std::cout << min << " " << repeatCounter << std::endl;

  return 0;
}
