#include <cassert>

class DNANucleobase final {
public:
    static DNANucleobase make_adenine() { return DNANucleobase(NucleobaseSymbol::A); }
    static DNANucleobase make_thymine() { return DNANucleobase(NucleobaseSymbol::T); }
    static DNANucleobase make_cytosine() { return DNANucleobase(NucleobaseSymbol::C); }
    static DNANucleobase make_guanine() { return DNANucleobase(NucleobaseSymbol::G); }

    DNANucleobase compliment() const {
        switch(s) {
            case NucleobaseSymbol::A: return make_thymine();
            case NucleobaseSymbol::C: return make_guanine();
            case NucleobaseSymbol::G: return make_cytosine();
            case NucleobaseSymbol::T: return make_adenine();
        }
        assert(false); //unreachable code
    }

    char as_symbol() const {
        switch(s) {
            case NucleobaseSymbol::A: return 'A';
            case NucleobaseSymbol::C: return 'C';
            case NucleobaseSymbol::G: return 'G';
            case NucleobaseSymbol::T: return 'T';
        }
        assert(false); //unreachable code
    }

    bool operator==(DNANucleobase base) const { return s == base.s; }
    bool operator!=(DNANucleobase base) const { return s != base.s; }

private:
    enum class NucleobaseSymbol {A, C, G, T};
    DNANucleobase(NucleobaseSymbol s): s(s) { }
    NucleobaseSymbol s;
};