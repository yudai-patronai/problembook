#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int main() {
    int n;
    cin >> n;
    auto *safe = new int[n + 3];
    safe[0] = 1;
    safe[1] = 3;
    for (int i = 2; i <= n; i++)
        safe[i] = 2 * safe[i - 1] + 2 * safe[i - 2];
    cout << safe[n] << endl;
    delete[] safe;
    return 0;
}
