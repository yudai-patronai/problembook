#include <iostream>

const int array_size = 30000;

int main()
{
	unsigned n;
	std::cin >> n;

	if (n == 1)
	{
		std::cout << 0 << std::endl;
		return 0;
	}

	bool flag[array_size];
	for (unsigned i = 0; i < array_size; ++i)
		flag[i] = false;

    for (unsigned i = 2; i <= n; ++i)
    {
        if (flag[i])
            continue;

        for (unsigned j = 2 * i; j <= n; j += i)
            flag[j] = true;
    }

    for (unsigned i = 2; i <= n; i++)
        if (!flag[i])
            std::cout << i << " ";

    std::cout << std::endl;

	return 0;
}