#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<vector<int>> threeSum(vector<int>& nums) {
    vector<vector<int>> result;
    if (nums.size() < 3)
        return result;
    sort(nums.begin(), nums.end());
    int n = nums.size()-1;

    for (int i = 0; i < nums.size() -2; i++) {
        if(i>0 && (nums[i]==nums[i-1]) )continue;
        int rest = -nums[i];
        int left = i+1;
        int right = nums.size() -1;

        while(left < right) {
            int check = nums[left]+nums[right];
            if (check > rest) {
                right--;
            }
            else if (check < rest) {
                left++;
            }
            else {
                vector<int>q{nums[i], nums[left], nums[right]};
                result.push_back(q);
                while(left < right && nums[left] == nums[left+1]){left++;}
                while(left < right && nums[right] == nums[right-1]){right--;}
                left++;
                right--;
            }
        }
        while(i < nums.size() -1 && nums[i + 1] == nums[i]){i++;}
    }
    return result;
}

void print(vector <vector<int>> vect) {
    for (int i = 0; i < vect.size(); i++) {
        for (int j = 0; j < 4; j++) {
            cout << vect[i][j] << " ";
        }
    }
    cout << endl;
}

int main() {
    int n = 0;
    std::cin >> n;
    vector<int> input(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> input[i];
    }
    vector <vector<int>> result = threeSum(input);
    print(result);
    return 0;
}


