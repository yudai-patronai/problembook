#include <iostream>

int main() {
  int n = 0;
  int min;
  int count = 1;

  std::cin >> n;

  std::cin >> min;

  for (int i = 1; i < n; ++i) {
    int input;
    std::cin >> input;

    if (min == input) {
      count++;
    } else if (min > input) {
      min = input;
      count = 1;
    }
  }

  std::cout << min << " " << count << std::endl;

  return 0;
}
