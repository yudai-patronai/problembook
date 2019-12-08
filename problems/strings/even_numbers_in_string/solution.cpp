#include <iostream>
#include <ctype.h>
#include <string>

int main()
{
  std::string in;
  std::getline(std::cin, in);
  int size = in.size();
  int count = 0;

  for (int i = 0; i < size; ++i) {
    if (isdigit(in[i]) && static_cast<int>(in[i]) % 2 == 0) {
      count++;
    }
  }
  std::cout << count << std::endl;
  return 0;
}
