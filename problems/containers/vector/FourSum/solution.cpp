#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

std::vector <std::vector<int>> quadr(std::vector<int> &nums, int target) {
    std::set<std::vector<int>> result;
    if (nums.size() < 4)
        return {};
    sort(nums.begin(), nums.end());
    for (int i = 0; i < static_cast<int>(nums.size()) - 3; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;

        for (int j = i + 1; j < static_cast<int>(nums.size()) - 2; j++) {
            if (j > i + 1 && nums[j] == nums[j - 1]) continue;
            int start = nums[i] + nums[j];
            int res = target - start;

            int k = j + 1;
            int p = static_cast<int>(nums.size()) - 1;

            while (k < p) {
                int check = nums[k] + nums[p];
                if (check > res) {
                    p--;
                }
                if (check < res) {
                    k++;
                }
                if (check == res) {
                    std::vector<int> quad{nums[i], nums[j], nums[k], nums[p]};
                    result.insert(quad);
                    do { k++; } while (k < p && nums[k] == nums[k - 1]);
                    do { p--; } while (k < p && nums[p] == nums[p + 1]);
                }
            }
        }
    }
    std::vector<std::vector<int>> a(result.begin(), result.end());
    return a;
}

void print(std::vector <std::vector<int>> vect) {
    for (int i = 0; i < static_cast<int>(vect.size()); i++) {
        for (int j = 0; j < 4; j++) {
            std::cout << vect[i][j] << " ";
        }
    }
    std::cout << std::endl;
}

int main() {
    int n = 0;
    std::cin >> n;
    std::vector<int> input(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> input[i];
    }
    int N;
    std::cin >> N;
    std::vector <std::vector<int>> result = quadr(input, N);
    print(result);
    return 0;
}


