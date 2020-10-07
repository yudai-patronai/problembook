
class Checker {
public:
    const size_t kPrime = 83886091ull; // ~10Mbytes bitset
    Checker() : bits(kPrime) {}
    void Add(const std::string& s) {
        bits[h1(s)] = true;
        bits[h2(s)] = true;
        bits[h3(s)] = true;
    }
    
    bool Exists(const std::string& s) {
        return (bits[h1(s)] && bits[h2(s)] && bits[h3(s)]);
    }
private:
    size_t h1(const std::string& s) {
        return h(s) % kPrime;
    }
    
    size_t h2(const std::string& s) {
        size_t raw = h(s);
        return ((raw << 4) ^ (raw >> 4)) % kPrime;
    }
    
    size_t h3(const std::string& s) {
        size_t raw = h(s);
        return ((raw << 16) ^ (raw >> 2)) % kPrime;
    }
    
    std::vector<bool> bits;
    std::hash<std::string> h;
};
