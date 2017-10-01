#include <iostream>
#include <ctype.h>
#include <string>

int main()
{
	std::string in;
	std::getline(std::cin, in);

	int count = 0;
	for(int i = 0; i < in.size(); ++i)
		if (isdigit(in[i]) && atoi(in[i]) % 2 == 0)
			count++;

	std::cout << count << std::endl;
	return 0;
}