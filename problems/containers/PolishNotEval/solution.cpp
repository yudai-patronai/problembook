#include <iostream>
#include <string>
#include <vector>
#include <stack>

int polish_not_eval(const std::vector <std::string> &tokens) {
    if (tokens.size() == 0)
        return -1;
    std::stack<int> s;
    for (auto &t : tokens)
        if (isdigit(t.back())) {
            s.push(stoi(t));
        } else {
            int n = s.top();
            s.pop();
            if (t == "+") s.top() += n;
            else if (t == "-") s.top() -= n;
            else if (t == "*") s.top() *= n;
            else if (t == "/") s.top() /= n;
        }
    return s.top();
}
std::vector<std::string> tokenize(const std::string &str, char delim) {
    std::vector<std::string> out;
    size_t start;
    size_t end = 0;

    while ((start = str.find_first_not_of(delim, end)) != std::string::npos) {
        end = str.find(delim, start);
        out.push_back(str.substr(start, end - start));
    }
    return out;
}

int main() {
    std::vector<std::string> tokens;
    std::string in;
    getline(std::cin, in);
    tokens = tokenize(in, ' ');
    std:: cout << polish_not_eval(tokens) <<std::endl;
    return 0;
}
