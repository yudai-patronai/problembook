
int main() {
    Checker c;
    const size_t kNumTests = 2000000;
    const size_t kMaxErrorPercent = 2;
    
    size_t interval, resok, res1, res2;
    std::cin >> interval >> resok >> res1 >> res2;
    //interval=146307;resok=15;res1=13;res2=23;
    
    std::vector<int8_t> v(47185920ull); // ~45 Mbytes
    
    for (size_t i = 0; i < 5000000; ++i) {
        c.Add(std::to_string(i * interval + resok));
    }
    
    size_t fp = 0, fn = 0;
    
    for (size_t i = 0; i < kNumTests; ++i) {
        if (!c.Exists(std::to_string(i * interval + resok))) {
            ++fn;
        }
        if (c.Exists(std::to_string(i * interval + res1))) {
            ++fp;
        }
        if (c.Exists(std::to_string(i * interval + res2))) {
            ++fp;
        }
    }
    
    if ((fp + fn) * 100 > kMaxErrorPercent * kNumTests * 3) {
        std::cerr << "Error rate: " << (static_cast<double>(fp + fn) * 100 / (kNumTests * 3)) << "%\n";
        std::cout << "NO\n";
    } else {
        std::cerr << "Error rate: " << (static_cast<double>(fp + fn) * 100 / (kNumTests * 3)) << "%\n";
        std::cout << "YES\n";
    }
}
