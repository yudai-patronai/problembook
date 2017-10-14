#include <iostream>
#include <string>

int main()
{
  std::string input;
  std::getline(std::cin, input);

  int counter = 0;
  for (int i = 0; i < input.size(); ++i)
  {
    if (input.at(i) == ' ')
      continue;

    input.at(i) = (counter % 2 == 0) ? toupper(input.at(i)) : tolower(input.at(i));
    counter++;
  }

  std::cout << input << std::endl;

  return 0;
}
