#include <iostream>

#define MIN(a, b) ((a < b) ? a : b)

int main()
{
	std::string input;
	std::getline(std::cin, input);
	for (unsigned i = 0; i < input.size(); ++i)
	{
		unsigned max_len = MIN(i, input.size() - 1 - i);
		unsigned len = 1;
		for (; len <= max_len; ++len)
		{
			if (input[i - len] != input[i + len])
				break;
		}

		std::cout << (len - 1) * 2 + 1 << ' ';
	}
	return 0;
}
