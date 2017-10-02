#include <iostream>

const unsigned MIN_SIZE = 3;

int main()
{
	std::string input;
	std::string result;

	bool first = true;
	while (std::getline(std::cin, input, ' '))
	{
		if (!first)
			result += ' ';
		else
			first = false;

		if (input.size() > MIN_SIZE)
		{
			result += input;
		}
	}

	std::cout << result;
	return 0;
}

