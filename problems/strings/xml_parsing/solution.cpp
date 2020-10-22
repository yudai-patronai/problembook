#include<iostream>
#include<string>
#include<vector>

enum class ParsingState {
    kInitial,
    kOpeningTag,
    kContent,
    kClosingTag,
    kTerminal
};

int main() {
    std::string xml;
    std::getline(std::cin, xml);
    std::vector<std::string> stack;
    int xml_length = static_cast<int>(xml.length());
    
    if (xml_length < 2) {
        std::cout << "NO" << std::endl;
        return 0;
    }
    if (xml[0] != '<' || xml[1] == '/') {
        std::cout << "NO" << std::endl;
        return 0;
    }

    int curr_pos = 0;
    ParsingState state = ParsingState::kInitial;
    while (curr_pos < xml_length) {
        if (state == ParsingState::kContent || state == ParsingState::kInitial) {
            size_t u_new_pos = xml.find('<', curr_pos);
            if (u_new_pos == std::string::npos) {
                std::cout << "NO" << std::endl;
                return 0;
            }
            int new_pos = static_cast<int>(u_new_pos);
            if (new_pos == xml_length - 1) {
                std::cout << "NO" << std::endl;
                return 0;
            }
            if (xml[new_pos + 1] == '/') {
                state = ParsingState::kClosingTag;
                curr_pos = new_pos + 2;
            } else {
                state = ParsingState::kOpeningTag;
                curr_pos = new_pos + 1;
            }
            continue;
        }
        if (state == ParsingState::kOpeningTag) {
            size_t u_new_pos = xml.find('>', curr_pos);
            if (u_new_pos == std::string::npos) {
                std::cout << "NO" << std::endl;
                return 0;
            }
            int new_pos = static_cast<int>(u_new_pos);
            stack.push_back(xml.substr(curr_pos, new_pos - curr_pos));
            curr_pos = new_pos + 1;
            state = ParsingState::kContent;
            continue;
        }
        if (state == ParsingState::kClosingTag) {
            size_t u_new_pos = xml.find('>', curr_pos);
            if (u_new_pos == std::string::npos) {
                std::cout << "NO" << std::endl;
                return 0;
            }
            int new_pos = static_cast<int>(u_new_pos);
            if (stack.back() != xml.substr(curr_pos, new_pos - curr_pos)) {
                std::cout << "NO" << std::endl;
                return 0;
            }
            stack.pop_back();
            curr_pos = new_pos + 1;
            if (static_cast<int>(stack.size()) > 0) {
                state = ParsingState::kContent;
            } else {
                state = ParsingState::kTerminal;
            }
            continue;
        }
        if (state == ParsingState::kTerminal) {
            std::cout << "NO" << std::endl;
            return 0;
        }
    }
    if (state != ParsingState::kTerminal) {
        std::cout << "NO" << std::endl;
        return 0;
    }
    std::cout << "YES" << std::endl;
    return 0;
}
