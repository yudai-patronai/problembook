#include <iostream>

const int MAX_N = 100000;

int main()
{
	int N, M;
	int array[MAX_N];

	std::cin >> N >> M;

	for (int i = 0; i < N; ++i)
	{
		std::cin >> array[i];
	}


	for (int i = M % N; i < N; ++i)
	{
		std::cout << array[i] << " ";
	}

	for (int i = 0; i < M % N; ++i)
	{
		std::cout << array[i] << " ";
	}
	std::cout << std::endl;

	return 0;
}
