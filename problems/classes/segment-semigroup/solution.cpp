#include <iostream>
#include <algorithm>

class Segment final {
public:
    Segment(): Segment(1,0) { }
    Segment(long long beg, long long end): beg(beg), end(end) { }

    bool contains(long long p) const { return p >= beg and p <= end; } 
    long long count() const { return empty() ? 0 : (end - beg + 1);}
    bool empty() const { return end < beg; }
    Segment const& print() const {
        if (empty())
            std::cout << "[]";
        else
            std::cout << "[" << beg << "," << end << "]";
        return *this;
    }

    Segment& intersect(Segment const &oth) {
        beg = std::max(beg,oth.beg);
        end = std::min(end,oth.end);
        return *this;
    }
private:
    long long beg, end;
};

Segment intersect(Segment const &lha, Segment const &rha) {
    Segment tmp(lha);
    return tmp.intersect(rha);
}