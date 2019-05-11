#include <iostream>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;
using std::floor;
using std::swap;

int main() {
    int n, k;

    cin >> n >> k;

    int *a = new int[n];
    int *b = new int[n];

    for (int i = 0; i < n; i++)
        std::cin >> a[i];

    for (int j = 0; j < k; j++) {
        for (int i = 0; i < n; i++)
            b[i] = floor((a[(i - 1 + n) % n] + a[i] + a[(i + 1) % n]) / 3.0);

        swap(a, b);
    }

    for (int i = 0; i < n; i++)
        cout << a[i] << ' ';

    cout << endl;

    delete[] a;
    delete[] b;

    return 0;
}
