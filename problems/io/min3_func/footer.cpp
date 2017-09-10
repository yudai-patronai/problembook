#include "header.cpp"

int main()
{
  int a = 0;
  int b = 0;
  int c = 0;

  std::cin >> a >> b >> c;

  std::cout << FindMin(a,b,c) << std::endl;

  return 0;
}

/*#include <iostream>
#include "header.h"

int main()
{
  int a = 0;
  int b = 0;
  int c = 0;

  std::cin >> a >> b >> c;

  std::cout << FindMin(a,b,c) << std::endl;

  return 0;
}

int FindMin(int a, int b, int c)
{
  int ret = a;

  if (ret > b)
    ret = b;

  if (ret > c)
    ret = c;

  return ret;
}*/
