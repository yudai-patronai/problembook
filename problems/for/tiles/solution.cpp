#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int main() {
    uint64_t n, res = 0;
    cin >> n;
    for (uint64_t i = 2; i <= n; i *= 2)
        res += n / i;
    cout << res << endl;
    return 0;
}
