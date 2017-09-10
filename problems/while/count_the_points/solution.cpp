#include <iostream>
#include <math.h>

int main()
{
  int data[4][4];
  // 0 - count
  // 1 - R
  // 2 - xR
  // 3 - yR

  for (int i = 0; i < 4; ++i)
    for (int j = 0; j < 4; j++)
      data[i][j] = 0;

  int number = 0;
  std::cin >> number;

  for (int i = 0; i < number; ++i)
  {
    int x;
    int y;
    std::cin >> x >> y;

    int quarterNum = -1;
    if (x * y != 0)
    {
      if (x > 0 && y > 0)
        quarterNum = 0; //first
      else if (x < 0 && y > 0)
        quarterNum = 1; //second
      else if (x < 0 && y < 0)
        quarterNum = 2; //third
      else
        quarterNum = 3; //fourth
    }
    else
      continue;

    data[quarterNum][0]++;

    if (data[quarterNum][0] == 1
      || abs(x) < data[quarterNum][1]
      || abs(y) < data[quarterNum][1])
      {
        data[quarterNum][1] = abs(x) < abs(y) ? abs(x) : abs(y);
        data[quarterNum][2] = x;
        data[quarterNum][3] = y;
      }
  }

  int quarterNum = 0;
  int max = data[0][0];
  for (int i = 1; i < 4; ++i)
  {
    if (data[i][0] > max
      || (data[i][0] == max && data[i][1] < data[quarterNum][1]))
    {
      max = data[i][0];
      quarterNum = i;
    }
  }

  std::cout << quarterNum + 1 << std::endl;
  std::cout << data[quarterNum][0] << std::endl;
  std::cout << data[quarterNum][2] << " " << data[quarterNum][3] << std::endl;
  std::cout << data[quarterNum][1] << std::endl;

  return 0;
}
