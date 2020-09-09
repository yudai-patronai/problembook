//
// Created by Olga on 09/09/2020.
//
//
// Created by Olga on 09/09/2020.
//
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> findArrayQuadruplet(vector<int> &num, int s)
{
    sort(arr.begin(), arr.end());

    if (arr.size() < 4)
        return {};
    cout <<"rr"<<endl;
    for (int i = 0; i < arr.size() - 3; i++) {
        for (int j = i + 1; j < arr.size() - 2; j++) {
            int rest = s - (arr[i] + arr[j]);
            int left = j+1;
            int rigth = arr.size() - 1;
            while(left < rigth) {
                cout << rest << endl;
                if (arr[left] + arr[rigth] < rest) {
                    left++;
                }
                else if (arr[left] + arr[rigth] > rest) {
                    rigth--;
                }
                else if (rest == arr[left] + arr[rigth]){
                    //cout <<arr[i] <<endl;
                    return {arr[i], arr[j], arr[left], arr[rigth]};
                }
            }
        }
    }
    return {};
}

int main() {
    int n = 0;
    std::cin >> n;
    vector<int> input(n);
    for(int i = 0; i < n; ++i){
        std::cin >> input[i];
    }
    int N;
    std::cin >> N;
    vector<int> result = findArrayQuadruplet(input, N);
    print(result);
    return 0;
}


