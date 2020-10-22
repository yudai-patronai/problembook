
int main() {

    std::string div5reg = GetRegex();
    std::regex div5(div5reg, std::regex_constants::nosubs | std::regex_constants::ECMAScript);
    std::cmatch m;
    
    std::stringstream ss;
    std::string s;
    ss << std::setbase(2);
    
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
