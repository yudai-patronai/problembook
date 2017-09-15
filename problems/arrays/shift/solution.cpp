#include <iostream>

int main()
{
	int N, M;
	std::cin >> N >> M;

	int* array = new int[N];

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

	delete[] array;

	return 0;
}
