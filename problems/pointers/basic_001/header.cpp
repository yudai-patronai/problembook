#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int* now_get_me_some_bytes(unsigned int n);
void now_free_some_bytes(int* p);

int main() {
    unsigned int n;
    cin >> n;
    int *a = now_get_me_some_bytes(n);
    for (unsigned int i = 0; i < n; i++)
        cin >> a[i];
    int s = 0;
    for (unsigned int i = 0; i < n; i++)
        s += a[i];
    if (s % 2)
        cout << "NO" << endl;
    else
        cout << "YES" << endl;
    now_free_some_bytes(a);
    return 0;
}
