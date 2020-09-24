#include <iostream>
#include <string>
#include <cassert>
#include <algorithm>
#include <iterator>
#include <vector>

DNANucleobase from_char(char s) {
    switch(s) {
        case 'A': return DNANucleobase::make_adenine();
        case 'C': return DNANucleobase::make_cytosine();
        case 'G': return DNANucleobase::make_guanine();
        case 'T': return DNANucleobase::make_thymine();
    }
    assert(false); //unreachable code
}

DNA from_string(std::string const &s) {
    DNA tmp;
    std::for_each(s.begin(),s.end(),[&tmp](char s) { tmp += from_char(s); } );
    return tmp;
}

std::istream& operator>>(std::istream &is, DNA &dna) {
    std::string dna_string;
    is >> dna_string;
    dna = from_string(dna_string);
    return is;
}

int main() {
    //simple tests for the methods to exist
    {
        DNA dna_empty;
        DNA dna_adenine(DNANucleobase::make_adenine());
        assert(dna_empty.empty());
        assert("[]" == dna_empty.as_string());
        assert("[A]" == dna_adenine.as_string());
        assert(dna_empty != dna_adenine);

        dna_empty += dna_adenine;
        assert(!dna_empty.empty());
        assert("[A]" == dna_empty.as_string());
        assert(dna_empty == dna_adenine);

        auto dna_sum = dna_empty + dna_adenine;
        assert("[AA]" == dna_sum.as_string());
        assert("[A]" == dna_empty.as_string());
        assert("[A]" == dna_adenine.as_string());

        dna_empty += dna_empty;
        assert("[AA]" == dna_empty.as_string());
        assert(dna_sum == dna_empty);

        assert("[TT]" == dna_sum.invert().as_string());
        assert("[TT]" == dna_sum.as_string());
        assert(dna_sum == dna_empty.invert());
    }

    //nucleobase sequences concatenation correctness test
    {
        int count;
        std::cin >> count;
        std::vector<DNA> dna_vec(count);
        std::istream_iterator<DNA> cin_it(std::cin);
        std::generate(dna_vec.begin(),dna_vec.end(),[&cin_it](){return *cin_it++;});

        DNA result_dna;
        for (auto &dna : dna_vec)
            result_dna += dna;
        std::cout << result_dna.invert().as_string() << std::endl;
    }
    
    return 0;
}