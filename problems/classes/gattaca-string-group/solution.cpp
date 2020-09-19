#include <string>
#include <vector>
#include <algorithm>
#include <iterator>

class DNA final {
public:
    DNA() { }
    DNA(DNANucleobase base): _dna(1,base) { }

    bool empty() const { return _dna.empty(); }

    std::string as_string() const {
        std::string dna_string;
        dna_string.reserve(_dna.size()+3);
        dna_string.push_back('[');
        std::transform(_dna.begin(),_dna.end(),std::back_inserter(dna_string),[](DNANucleobase base){ return base.as_symbol(); });
        dna_string.push_back(']');
        return dna_string;
    }

    bool operator==(DNA const &oth) const {
        if (_dna.size() != oth._dna.size()) return false;
        if (_dna.empty() and oth.empty()) return true;

        std::vector<bool> compare_each;
        compare_each.reserve(_dna.size());
        std::transform(_dna.begin(),_dna.end(),oth._dna.begin(),std::back_inserter(compare_each),[](DNANucleobase lha, DNANucleobase rha) { return lha == rha; });
        return std::all_of(compare_each.begin(),compare_each.end(),[](bool b) { return b; });
    }

    bool operator!=(DNA const &oth) const {
        return !(*this == oth);
    }

    DNA& invert() {
        std::transform(_dna.begin(),_dna.end(),_dna.begin(),[](DNANucleobase base){ return base.compliment(); });
        std::reverse(_dna.begin(),_dna.end());
        return *this;
    }

    DNA& operator+=(DNA const &rha) {
        _dna.reserve(_dna.size() + rha._dna.size());

        auto lha_it = _dna.rbegin();
        auto lha_end = _dna.rend();
        auto rha_it = rha._dna.begin();
        auto rha_end = rha._dna.end();
        for (; lha_it != lha_end and rha_it != rha_end and *lha_it == rha_it->compliment(); ++lha_it, ++rha_it);
        
        std::vector<DNANucleobase> dna_result;
        dna_result.reserve(_dna.size() + rha._dna.size());
        std::copy(_dna.begin(),lha_it.base(),std::back_inserter(dna_result));
        std::copy(rha_it,rha_end,std::back_inserter(dna_result));
        _dna.swap(dna_result);

        return *this;
    }

private:
    std::vector<DNANucleobase> _dna;
};

DNA operator+(DNA const &lha, DNA const &rha) {
    DNA tmp(lha);
    return tmp += rha;
}

