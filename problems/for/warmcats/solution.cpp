#include <iostream>
using std::cin;
using std::cout;
using std::endl;
const int N = 30;

int main() {
    char tiles[N] = {0};
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int pos, len;
        cin >> pos >> len;
        for (int j = pos; j < pos + len; j++)
            tiles[j] = 1;
    }
    int tlen;
    cin >> tlen;
    int hlen = 0;
    for (int i = 0; i < N; i++) {
        if (tiles[i] == 0) {
            hlen++;
            if (hlen == tlen) {
                cout << i - tlen + 1 << endl;
                return 0;
            }
        }
        else
            hlen = 0;
    }
    cout << -1 << endl;
    return 0;
}
