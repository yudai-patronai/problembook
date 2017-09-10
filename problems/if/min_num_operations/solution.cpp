#include <iostream>

int Calculate(int degree)
{
  if (degree == 1)
		return 0;
	if (degree % 2 == 1)
		return Calculate(degree - 1) + 1;
	else
  {
		return Calculate(degree / 2) + 1;
	}
}

int main()
{
  int degree = 0;

  std::cin >> degree;

  std::cout << Calculate(degree) << std::endl;

  return 0;
}
