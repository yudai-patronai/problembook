#include <iostream>
#include <vector>
#include <string>
#include <queue>

const char kAlphabetMin = 'a';
const char kEpsilon = 'E';

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
        
        closures.resize(n_states);
        for (uint16_t state = 0; state < n_states; ++state) {
            closures[state] = (1ull << state);
        }
    }
    
    bool IsGood(const std::string& s) const {
        uint64_t current_state = closures[0];
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
        if (c == kEpsilon) {
            closures[from] |= closures[to];
        } else {
            transitions[from][c - kAlphabetMin] |= (1ull << to);
        }
    }
    
    void BuildEpsilonClosure() {
        // This is not an optimal e-closure calculation way
        // But as long as number of states is limited to 64,
        // N^3  =  262 144  <  1 000 000
        // So just don't care
        
        for (uint16_t state = 0; state < size; ++state) {
            ComputeEpsilonClosureForState(state);
        }
        
        for (uint16_t state = 0; state < size; ++state) {
            for (uint16_t c = 0; c < alphabet_size; ++c) {
                for (uint16_t other = 0; other < size; ++other) {
                    if (transitions[state][c] & (1ull << other)) {
                        transitions[state][c] |= closures[other];
                    }
                }
            }
        }
    }
    
    void ComputeEpsilonClosureForState(int16_t state) {
        std::queue<int16_t> q;
        uint64_t seen = (1ull << state);
        q.push(state);
        
        while(!q.empty()) {
            int16_t cur = q.back();
            for (int16_t mb_state = 0; mb_state < size; ++mb_state) {
                uint64_t mb_mask = (1ull << mb_state);
                if ((closures[cur] & mb_mask) && (!(seen & mb_mask))) {
                    q.push(mb_state);
                }
            }
            seen |= closures[cur];
            q.pop();
        }
        
        closures[state] = seen;
    }
    
    std::vector<std::vector<uint64_t>> transitions;
    uint64_t terminals;
    uint16_t alphabet_size, size;
    std::vector<uint64_t> closures;
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
    
    aut.BuildEpsilonClosure();   
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
