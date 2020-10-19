
bool testClassNotBroken() {
    {
        TimeOfDay t{1, 2, 3};
        
        if ((t.hour != 1) || (t.minute != 2) || (t.second != 3)) { return false; }
        if (!t.IsAM()) { return false; }
        if (t.IsPM()) { return false; }
        if (!t.IsValid()) {return false;}
    }
    
    {
        TimeOfDay t{21, 12, 33};
        
        if ((t.hour != 21) || (t.minute != 12) || (t.second != 33)) { return false; }
        if (t.IsAM()) { return false; }
        if (!t.IsPM()) { return false; }
        if (!t.IsValid()) {return false;}
    }
    
    {
        TimeOfDay t{24, 60, 60};
        
        if (t.IsAM()) { return false; }
        if (t.IsPM()) { return false; }
        if (t.IsValid()) {return false;}
    }
    
    return true;
}

std::vector<TimeOfDay> makeRandomTimes(size_t sz) {
    std::random_device rd;
    std::mt19937 gen(rd());    
    std::uniform_int_distribution<uint8_t> hours(0, 23), min_sec(0, 59); 
    std::vector<TimeOfDay> seq;
    seq.reserve(sz);
    for (size_t i = 0; i < sz; ++i) {
        seq.emplace_back(hours(gen), min_sec(gen), min_sec(gen));
    }
    return seq;
}

template<class SetType>
bool testSet(const std::vector<TimeOfDay>& tests) {
    SetType fp_set;
    fp_set.insert({1, 2, 3});
    fp_set.insert({1, 2, 4});
    fp_set.insert({1, 3, 3});
    fp_set.insert({2, 2, 3});
    
    if (fp_set.find({2, 3, 3}) != fp_set.end()) { return false; }
    if (fp_set.find({3, 2, 3}) != fp_set.end()) { return false; }
    if (fp_set.find({1, 3, 2}) != fp_set.end()) { return false; }
    if (fp_set.find({3, 2, 1}) != fp_set.end()) { return false; }
    
    SetType maybe_set;
    for (const auto& t : tests) {
        maybe_set.insert(t);
    }
    
    for (const auto& t : tests) {
        if (maybe_set.find(t) == maybe_set.end()) {
            return false;
        }
    }
    
    return true;
}

int main() {
    const size_t kNumTests = 1000;
    std::vector<TimeOfDay> set_tests = makeRandomTimes(kNumTests);
    
    if (testClassNotBroken() &&
        testSet<std::set<TimeOfDay>>(set_tests) && 
        testSet<std::unordered_set<TimeOfDay>>(set_tests)) {
        std::cout << "YES\n";
    } else {
        std::cout << "NO\n";
    }    
} 
