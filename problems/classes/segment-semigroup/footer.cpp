#include <iostream>

std::istream& operator>>(std::istream &is, Segment &s) {
    long long beg, end;
    is >> beg >> end;
    s = end < beg ? Segment() : Segment(beg,end);
    return is;    
}

#include <iterator>
#include <numeric>

int main() {
    std::istream_iterator<Segment> cin_it(std::cin);
    std::istream_iterator<Segment> cin_end;

    std::cout << std::accumulate(cin_it,cin_end,*cin_it,[](Segment const &acc, Segment const &next) { return intersect(acc,next);}).print().count();
    return 0;
}