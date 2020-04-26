#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int main() {
    int n;
    cin >> n;
    auto *safe = new int[n + 3];
    safe[0] = 1;
    safe[1] = 2;
    safe[2] = 4;
    for (int i = 3; i <= n; i++)
        safe[i] = safe[i - 1] + safe[i - 2] + safe[i - 3];
    cout << safe[n] << endl;
    delete[] safe;
    return 0;
}
