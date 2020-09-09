//
// Created by Olga on 09/09/2020.
//
#include <iostream>
#include <vector>
using namespace std;

void print(vector<int> &result) {
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] <<" ";
    }
    cout <<endl;
}
vector<int> twoSum(vector<int> &nums, int target) {
    vector<int> result;
    for (int i = 0; i < nums.size() -1; i++) {
        for (int j = i+1; i < nums.size(); j++) {
            if (nums[j] == target - nums[i]) {
                result.push_back(i);
                result.push_back(j);
                return result;
            }
        }
    }
    return result;
}

int main() {
    int n = 0;
    std::cin >> n;
    vector<int> input(n);
    for(int i = 0; i < n; ++i){
        std::cin >> input[i];
    }
    int N = 9;
    std::cin >> N;
    vector<int> result = twoSum(input, N);
    print(result);
    return 0;
}
