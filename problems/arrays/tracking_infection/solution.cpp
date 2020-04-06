#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    char rooms[100] = {0};
    rooms[0] = 1;
    uint64_t n;
    int haz = 0;
    cin >> n;
    int *f = new int[n];
    int *t = new int[n];
    for (uint64_t i = 0; i < n; i++)
        cin >> f[i] >> t[i];
    for (uint64_t i = 0; i < n; i++) {
        if (rooms[f[n - 1 - i]])
            rooms[t[n - 1 - i]] = 1;
    }
    for (int i = 0; i < 100; i++)
        haz += rooms[i];
    cout << haz <<endl;
    delete[] f;
    delete[] t;
    return 0;
}
