#include <iostream>
#include <vector>
#include <string>

const char kAlphabetMin = 'a';

class Automaton {
public:
    const int16_t kTrashState = -1;
    Automaton() = delete;
    Automaton(uint16_t alpha_size, uint16_t n_states)
    : alphabet_size(alpha_size), size(n_states) {
        transitions.resize(n_states);
        for (auto& col: transitions) {
            col.resize(alpha_size, kTrashState);
        }
        
        is_terminal.resize(n_states, false);
    }
    
    bool IsGood(const std::string& s) const {
        int16_t current_state = 0;
        for (char c : s) {
            current_state = transitions[current_state][c - kAlphabetMin];
            if (current_state == kTrashState) {
                return false;
            }
        }
        return (is_terminal[current_state]);
    }
private:
    friend Automaton ReadAutomaton();
    
    void AddTerminal(uint16_t state) {
        is_terminal[state] = true;
    }
    
    void AddTransition(uint16_t from, uint16_t to, char c) {
        transitions[from][c - kAlphabetMin] = to;
    }
    
    std::vector<std::vector<int16_t>> transitions;
    std::vector<bool> is_terminal;
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
    for (uint16_t i = 0; i < n; ++i) {
        std::cin >> from >> to >> c;
        aut.AddTransition(from, to, c);
    }
    
    std::cin >> n;
    for (uint16_t i = 0; i < n; ++i) {
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
