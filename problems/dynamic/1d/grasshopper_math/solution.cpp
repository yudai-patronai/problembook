#include <iostream>
#include <vector>
#include <algorithm>
using std::cin;
using std::cout;
using std::endl;
using std::vector;

int main() {
    int n;
    cin >> n;
    vector<int> squares(n);
    std::for_each(squares.begin(), squares.end(), [](int &x){ std::cin >> x; });
    vector<int> ways(n, 0);
    ways[0] = 1;
    for (int i = 0; i < n - 1; i++) {
        ways[i + 1] = (ways[i + 1] + ways[i]) % 937;
        if (squares[i] > 1 && i + squares[i] < n)
            ways[i + squares[i]] = (ways[i + squares[i]] + ways[i]) % 937;
    }
    cout << ways[n - 1] << endl;
    return 0;
}
