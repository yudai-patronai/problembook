#include <iostream>
using std::cout;
using std::cin;
using std::endl;


int main() {
    int a, b;
    cin >> a >> b;
    cout << do_some_awesome_work(&a, &b) <<endl;
    return 0;
}
