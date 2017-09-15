#include <iostream>

void sort(int *array, int begin, int end)
{
	int hi = begin;
	int ti = end;

	int pivot = array[ti];
	while (hi <= ti)
	{
		while (array[hi] < pivot)
			++hi;

		while (array[ti] > pivot)
			--ti;

		if (hi <= ti)
		{
			int tmp = array[hi];
			array[hi] = array[ti];
			array[ti] = tmp;

			++hi;
			--ti;
		}
	}

	if (ti > begin)
		sort(array, begin, ti);
	if (hi < end)
		sort(array, hi , end);
}

int main()
{
	int N;
	std::cin >> N;

	int* array = new int[N];

	for (int i = 0; i < N; ++i)
	{
		std::cin >> array[i];
	}

	sort(array, 0, N - 1);

	for (int i = 0; i < N; ++i)
	{
		std::cout << array[i] << " ";
	}
	std::cout << std::endl;

	delete[] array;

	return 0;
}
