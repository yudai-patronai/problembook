
#include <iostream>

using std::cin;
using std::cout;
using std::endl;


int main()
{
    bool a, c, d, e, f, g, h, i, j;
    float b;
    cin >> a >> b >> c >> d >> e >> f >> g >> h >> i >> j;

    int group = 0;
    if (a || b >= 37.5) {
        if (c) {
            if (d)
                group = 1;
            else
                group = 2;
        }
        else {
            if (e || f)
                group = 2;
            else if (g)
                group = 2;
            else
                group = 3;
        }
    }
    else {
        if (c) {
            if (i || j)
                group = 2;
            else if (e || f)
                group = 3;
            else
                group = 4;
        }
        else if (g || h)
            group = 3;
        else
            group = 4;
    }

    cout << group << endl;

    return 0;
}

