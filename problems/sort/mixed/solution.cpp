#include <iostream>
#define COUT std::cout
#define CIN std::cin


void printar(int* arr, int n) {
    int i;
    for (i = 0; i < n; ++i) {
        COUT << arr[i] << " ";
    }
    COUT << "\n";
}
int main() {
    int n, temp;
    CIN >> n;
    int* arr;
    arr = new int[n];
    int i, j, chg = 0, pp = -1, pn = -1;
    for (i = 0; i < n; ++i) {
        CIN >> arr[i];
    }
    for (j =0; j < n; ++j) {
    chg = 0;
    pp = -1;
    pn = -1;
    for (i = 0; i < n; ++i) {
        if (arr[i] >= 0) {
            if ((pp >= 0)&&(arr[i] < arr[pp])) {
                temp = arr[i];
                arr[i] = arr[pp];
                arr[pp] = temp;
                printar(arr, n);
                chg += 1;
            }
            pp = i;
        } else {
            if ((pn >= 0)&& (arr[i] > arr[pn])) {
                temp = arr[i];
                arr[i] = arr[pn];
                arr[pn] = temp;
                printar(arr, n);
                chg += 1;
                }
            pn = i;
        }
    }
    if (chg == 0) {
        break;
    }
    }
    return 0;
}
