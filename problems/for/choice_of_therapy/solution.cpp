#include <iostream>
#include <cstdlib>
#include <cmath>

int simple_check(int sum){
  for(int i = 2; i <= sqrt(sum); ++i)
    if(sum % i == 0)
        return 0;
  return 1;
}

int main(){
  int n = 0;
  std::cin >> n;
  int *drugs = new int[n];
  for(int i = 0; i < n; ++i){
    std::cin >> drugs[i];
  }
  int max_sum = 0;
  int sum = 0;
  for(int i = 0; i < n - 1; ++i){
    for(int j = i + 1; j < n; ++j){
      sum = drugs[i] + drugs[j];
      if(simple_check(sum) && sum > max_sum)
        max_sum = sum;
    }
  }
  if(max_sum > 0)
    std::cout << max_sum << std::endl;
  else
    std::cout << 0 << std::endl;
  return 0;
}
