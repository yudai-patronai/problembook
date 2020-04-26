#include <iostream>
#include <vector>
#include <algorithm>
using std::cin;
using std::cout;
using std::endl;
using std::vector;

int main() {
    int tmp;
    vector<int> coord;
    while (cin >> tmp)
        coord.push_back(tmp);
    if (coord.size() == 2) {
        cout << coord[1] - coord[0] << endl;
        return 0;
    }
    vector<int> dist(coord.size(), 0);
    std::sort(coord.begin(), coord.end());
    dist[1] = coord[1] - coord[0];
    dist[2] = coord[2] - coord[0];
    for (unsigned i = 3; i < coord.size(); i++)
        dist[i] = coord[i] - coord[i - 1] +
            (dist[i - 2] < dist[i - 1] ? dist[i - 2] : dist[i - 1]);
    cout << dist[coord.size() - 1] << endl;
    return 0;
}
