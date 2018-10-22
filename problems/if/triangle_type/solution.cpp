#include <iostream>
#include <cmath>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    if ((a+b <= c) || (abs(a-b) >= c)) {
        std::cout << "impossible";
        return 0;
    }

    if ((a*a + b*b == c*c) || (c*c + b*b == a*a) || (a*a + c*c == b*b)) {
        std::cout << "right";
        return 0;
    }

    if ((a*a + b*b > c*c) || (c*c + b*b > a*a) || (a*a + c*c >  b*b)) {
        std::cout << "obtuse";
        return 0;
    }

    std::cout << "acute";
    return 0;
}
