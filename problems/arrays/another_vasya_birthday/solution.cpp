#include <iostream>

int main()
{
	unsigned n;

	std::cin >> n;
	unsigned array[n];
	for(unsigned i = 0; i < n; ++i)
		std::cin >> array[i];
	
	//bubble
	for(unsigned i = 0; i < n; ++i)
		for(unsigned j = 1; j < n; ++j)
			if (array[j] < array[j - 1])
			{
				unsigned temp = array[j];
				array[j] = array[j - 1];
				array[j - 1] = temp;
			}

	unsigned stoneOut = 0;
	for(unsigned i = 1; i < n; ++i)
		if (array[i - 1] ==  array[i])
			stoneOut++;

	std::cout << (stoneOut > 1 ? 0 : 1) << std::endl;

	return 0;
}