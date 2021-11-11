#include <iostream>
#include <iomanip>
#include <map>

struct Date final {
    int day, month, year;
    Date(): Date(0,0,0) { }
    Date(int day, int month, int year): day(day), month(month), year(year) { }
};

std::ostream& operator<<(std::ostream &os, Date const &d) {
    return os << std::setw(2) << d.day << '.' << std::setw(2) << d.month << '.' << d.year;
}

std::istream& operator>>(std::istream &is, Date &d) {
    char tmp;
    return is >> d.day >> tmp >> d.month >> tmp >> d.year;
}

bool operator<(Date const &lha, Date const &rha) {
    return lha.year != rha.year ? lha.year < rha.year : (lha.month != rha.month ? lha.month < rha.month : lha.day < rha.day);
}

int main() {
    using namespace std;

    cout << setfill('0');

    multimap<Date,unsigned> events_base;

    unsigned N;
    cin >> N;

    for (unsigned cnt = 0; cnt != N; ++cnt) {
        Date d;
        unsigned e;
        cin >> d >> e;
        events_base.insert(make_pair(d,e));
    }

    {
        unsigned rolling_max = events_base.begin()->second;
        for (auto it = events_base.begin(); it != events_base.end(); ++it)
            it->second = rolling_max = it->second > rolling_max ? it->second : rolling_max;
    }
    
    unsigned M;
    cin >> M;    

    for (unsigned cnt = 0; cnt != M; ++cnt) {
        Date d;
        cin >> d;
        if (d < events_base.begin()->first) {
            cout << 0 << endl;
            continue;
        }

        if (events_base.rbegin()->first < d) {
            cout << events_base.rbegin()->second << endl;
            continue;
        }

        auto it = prev(events_base.upper_bound(d));
        cout << it->second << endl;
    }

    return 0;
}