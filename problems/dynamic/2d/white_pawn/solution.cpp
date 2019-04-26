#include <iostream>
#include <string>

int main() {
    int n;
    std::cin >> n;
    int d[8][8] = {{0}};
    std::string s;
    for (int i = 0; i < n; i++) {
        std::cin >> s;
        d[static_cast<int>(s[1]) - static_cast<int>('1')]
         [static_cast<int>(s[0]) - static_cast<int>('a')] = 1;
    }
    std::cin >> s;
    int i0 = static_cast<int>(s[1]) - static_cast<int>('1');
    int j0 = static_cast<int>(s[0]) - static_cast<int>('a');
    for (int j = 0; j < 8; j++) {
        d[i0][j] = 0;
    }
    d[i0][j0] = 1;
    for (int i = i0+1; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (d[i][j] == 1) {
                d[i][j] = 0;
                if (j > 0) {
                    d[i][j] += d[i - 1][j - 1];
                }
                if (j < 7) {
                    d[i][j] += d[i - 1][j + 1];
                }
            } else {
                d[i][j] = d[i - 1][j];
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < 8; i++) {
        ans += d[7][i];
    }
    std::cout << ans << '\n';
    return 0;
}
