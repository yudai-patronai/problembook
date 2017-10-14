int main()
{
  int size;
  std::cin >> size;

  int *arr = new int[size];
  for(int i = 0; i < size; ++i)
  	std::cin >> arr[i];

  SortArray(arr, size);

  for(int i = 0; i < size; ++i)
  	std::cout << arr[i] << " ";

  std::cout << std::endl;

  delete[] arr;
  return 0;
}
