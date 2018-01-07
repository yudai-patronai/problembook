#include <iostream>
#include <fstream>

int main()
{
	std::ifstream in;
	unsigned count = 0;
	std::string tmp;

	in.open("input.txt");
	while (in >> tmp)
	{
		++count;
	}

	std::cout << count << std::endl;

	in.close();
	return 0;
}
