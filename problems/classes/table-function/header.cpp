#include <utility>

using ArgVal = std::pair<double,double>;

double interpolate(ArgVal left, ArgVal right, double inner_point) {
    return (right.second - left.second) / (right.first - left.first) * (inner_point - left.first) + left.second;
}
