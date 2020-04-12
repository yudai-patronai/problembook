
#include <iostream>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;

struct age_stat {
    unsigned cases;
    unsigned deaths;
    unsigned recovers;
};

int main()
{
    age_stat stats[150] = {};

    while (true) {
        unsigned age, result;
        cin >> age >> result;
        if (result == 3 || age >= 150)
            break;
        else if (result == 0) {
            stats[age].cases++;
            stats[age].deaths++;
        }
        else if (result == 1)
            // Do not track ill cases
            ;
        else if (result == 2) {
            stats[age].cases++;
            stats[age].recovers++;
        }
    }

    for (int i = 0; i < 150; i++)
        if (stats[i].cases)
            cout << i << " " << (int) round(100 * stats[i].recovers / (float) stats[i].cases) << endl;;

    return 0;
}

