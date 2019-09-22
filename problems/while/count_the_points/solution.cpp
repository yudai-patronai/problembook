#include <iostream>

int main() {
  int count1, count2, count3, count4;
  count1 = count2 = count3 = count4 = 0;

  int number = 0;
  std::cin >> number;

  for (int i = 0; i < number; ++i) {
    int x, y;
    std::cin >> x >> y;

    if (x * y != 0) {
      if (x > 0 && y > 0)
        count1++;  // first
      else if (x < 0 && y > 0)
        count2++;  // second
      else if (x < 0 && y < 0)
        count3++;  // third
      else
        count4++;  // fourth
    }
  }

  if (count1 >= count2 && count1 >= count3 && count1 >= count4)
    std::cout << "1 " << count1;
  else if (count2 >= count1 && count2 >= count3 && count2 >= count4)
    std::cout << "2 " << count2;
  else if (count3 >= count1 && count3 >= count2 && count3 >= count4)
    std::cout << "3 " << count3;
  else if (count4 >= count1 && count4 >= count2 && count4 >= count3)
    std::cout << "4 " << count4;
  else
      std::cout << "impossible error";
  std::cout << std::endl;

  return 0;
}
