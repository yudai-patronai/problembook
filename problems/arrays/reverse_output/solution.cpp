#include <iostream>

int main()
{
  int n = 0;

  std::cin >> n;

  int a[n];
  for (int i = 0; i < n; ++i)
    a[i] = 0;

  for(int i = 0; i < n; i++)
    std::cin >> a[i];

  for(int i = 1; i <= n; ++i)
    std::cout << a[n - i] << " ";

  std::cout << std::endl;

  return 0;
}
