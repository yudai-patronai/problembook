#include <vector>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <iomanip>

namespace jts {
    std::vector<ArgVal> read_arg_val_vector() {
        unsigned count;
        std::cin >> count;
        std::vector<ArgVal> result(count,ArgVal(0.,0.));
        std::generate(result.begin(),result.end(),[](){ ArgVal argval; std::cin >> argval.first >> argval.second; return argval; });
        return result;

    } 

    std::vector<double> read_args_vector() {
        unsigned count;
        std::cin >> count;
        std::istream_iterator<double> cin_it(std::cin);
        std::vector<double> args(count,0);
        std::generate(args.begin(),args.end(),[&cin_it](){ return *cin_it++; });
        return args;
    }

    void write_val_vector(std::vector<double> const &vals) {
        std::for_each(vals.begin(),vals.end(),[](double d) { std::cout << d << " ";});
        std::cout << std::endl;
    }
}

int main() {
    {
        std::cout << std::setprecision(2) << std::fixed;
        TableFunction f(jts::read_arg_val_vector());
        std::vector<double> args = jts::read_args_vector();
        std::vector<double> vals(args.size(),0);
        std::transform(args.begin(),args.end(),vals.begin(),f);
        std::for_each(vals.begin(),vals.end(),[](double d) { std::cout << d << " "; });
        std::cout << std::endl;
    }
    return 0;
}