#include <iostream>
#include <vector>
#include <string>

const char kAlphabetMin = 'a';

class Automaton {
public:
    const uint16_t kTrashState = 0;
    Automaton() = delete;
    Automaton(uint16_t alpha_size, uint16_t n_states)
    : alphabet_size(alpha_size), size(n_states) {
        terminals = 0;
        transitions.resize(n_states);
        for (auto& col: transitions) {
            col.resize(alpha_size, kTrashState);
        }
    }
    
    bool IsGood(const std::string& s) const {
        uint64_t current_state = 1;
        for (char c : s) {
            uint64_t tmp = 0;
            for (int16_t mb_state = 0; mb_state < size; ++mb_state) {
                if (current_state & (1ull<<mb_state)) {
                    tmp |= transitions[mb_state][c - kAlphabetMin];
                }
            }
            current_state = tmp;
            if (current_state == kTrashState) {
                return false;
            }
        }
        return (terminals & current_state);
    }
private:
    friend Automaton ReadAutomaton();
    
    void AddTerminal(uint16_t state) {
        terminals |= (1ull << state);
    }
    
    void AddTransition(uint16_t from, uint16_t to, char c) {
        transitions[from][c - kAlphabetMin] |= (1ull << to);
    }
    
    std::vector<std::vector<uint64_t>> transitions;
    uint64_t terminals;
    uint16_t alphabet_size, size;
}; 

Automaton ReadAutomaton() {
    uint16_t alphabet_size, n_states;
    
    std::cin >> alphabet_size >> n_states;
    Automaton aut(alphabet_size, n_states);
    
    size_t n;
    std::cin >> n;
    
    uint16_t from, to;
    char c;
    for (size_t i = 0; i < n; ++i) {
        std::cin >> from >> to >> c;
        aut.AddTransition(from, to, c);
    }
    
    std::cin >> n;
    for (size_t i = 0; i < n; ++i) {
        std::cin >> from;
        aut.AddTerminal(from);
    }
    
    return aut;
}

int main() {
    Automaton a = ReadAutomaton();
    size_t n_strings;
    std::cin >> n_strings;
    std::string s;
    for (size_t i = 0; i < n_strings; ++i) {
        std::cin >> s;
        std::cout << (static_cast<int>(a.IsGood(s))) << " ";
    }
}
