#include <iostream>
using std::cin;
using std::cout;
using std::endl;

void print_array(int* p);

int main() {
    int a[6];
    for (int i = 0; i < 6; i++)
        cin >> a[i];
    print_array(a);
    return 0;
}

