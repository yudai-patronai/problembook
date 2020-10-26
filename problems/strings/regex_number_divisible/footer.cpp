
int main() {

    std::string div5reg = GetRegex();
    std::regex div5(div5reg, std::regex_constants::nosubs | std::regex_constants::ECMAScript);
    std::cmatch m;
    
    std::stringstream ss;
    std::string s;
    ss << std::setbase(2);
    
    int n;
    std::cin >> n;
    
    if (n == 0) {
        if(!std::regex_match("101", div5)) {
            std::cout << "NO";
        } else {
            std::cout << "YES";
        }
    }
    
    if (n == 1) {
        if(!std::regex_match("1010", div5)) {
            std::cout << "NO";
        } else {
            std::cout << "YES";
        }
    }
    
    if (n == 2) {
        if(std::regex_match("1", div5)) {
            std::cout << "NO";
        } else {
            std::cout << "YES";
        }
    }
    
    if (n > 2) {
        {
            std::cin >> n;
            std::vector<int8_t> v(n);
            
            for (auto i = 0; i < n; ++i) {
                std::cin >> v[i];
            }
            std::cout << "Token: " << std::hex << Integrity::generate(&v[0], n) << "\n";
        }
        
        std::vector<size_t> failed_tests;
        
        for (size_t i = (1 << 15); i < (1<<16) - 1; ++i) {
            ss << std::bitset<16>(i);
            s = ss.str();
            ss.str("");
            
            if (((i % 5) == 0) != std::regex_match(s, div5)) {
                failed_tests.push_back(i);
            }
        }
        
        if(!std::regex_match("0", div5)) {
            failed_tests.push_back(0);
        }
        
        if (failed_tests.size()) {
            std::cerr << "Number of failed tests: " << failed_tests.size() << "\n";
            std::cerr << "Failed tests (max. 5):  ";
            for (size_t i = 0; i < 5; ++i) {
                if (i < failed_tests.size()) {
                    std::cerr << failed_tests[i] << " ";
                }
            }
            std::cerr << "\n";
            std::cout << "NO\n";
        } else {
            std::cout << "YES\n";
        }
    }
    
    
}
