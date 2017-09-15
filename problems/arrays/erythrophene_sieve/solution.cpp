#include <iostream>

int main()
{
	unsigned n;
	std::cin >> n;

	if (n == 1)
	{
		std::cout << 0 << std::endl;
		return 0;
	}

	unsigned primes[n];
	for(unsigned i = 0; i < n; ++i)
		primes[i] = 0;
	primes[0] = 2;

	unsigned primesSize = 1;
	for (unsigned i = 3; i <= n; ++i)
	{
		bool isPrime = true;
		for(unsigned j = 0; j < primesSize; ++j)
			if (i % primes[j] == 0)
			{
				isPrime = false;
				break;
			}
		
		if (isPrime)
		{
			primes[primesSize] = i;
			primesSize++;
		}
	}
	
	for(unsigned i = 0; i < primesSize; ++i)
		std::cout << primes[i] << " ";

	std::cout << std::endl;

	return 0;
}