#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main() {
    int n;

    cin >> n;

    auto dict = new string[n];

    for (int i = 0; i < n; i++)
        cin >> dict[i];


    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cout << dict[x];

        if (i != n-1)
            cout <<  ' ';
    }

    delete[] dict;

    return 0;
}
