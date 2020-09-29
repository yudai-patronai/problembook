#include <array>
#include <cassert>
#include <iostream>
#include <iterator>
#include <utility>
#include <vector>

enum class Letter : int { A,
                          C,
                          G,
                          T };
char to_char(Letter l) {
    switch (l) {
        case Letter::A: return 'A';
        case Letter::C: return 'C';
        case Letter::G: return 'G';
        case Letter::T: return 'T';
    }
    assert(false);  // unreachable code
}
Letter from_char(char ch) {
    switch (ch) {
        case 'A': return Letter::A;
        case 'C': return Letter::C;
        case 'G': return Letter::G;
        case 'T': return Letter::T;
    }
    assert(false);  // unreachable code
}

using State = unsigned;
using Config = std::pair<State, Letter>;
using Automaton = std::vector<std::array<Config, 4>>;

std::string code(Automaton const &automaton, std::string const &data) {
    State curr_state = 0;
    std::string result;
    result.reserve(data.size());
    std::transform(data.begin(), data.end(), std::back_inserter(result), [&automaton, &curr_state](char ch) {
        auto cfg = automaton[curr_state][static_cast<int>(from_char(ch))];
        curr_state = cfg.first;
        return to_char(cfg.second);
    });
    return result;
}

int main() {
    unsigned number_of_states;
    std::cin >> number_of_states;
    Automaton reversed_automaton(number_of_states);
    for (unsigned counter = 0; counter != number_of_states * 4; ++counter) {
        State from, to;
        char ch_read, ch_write;
        std::cin >> from >> ch_read >> to >> ch_write;
        Letter read = from_char(ch_read), write = from_char(ch_write);
        reversed_automaton[from - 1][static_cast<int>(write)] = Config(to - 1, read);
    }

    std::string encoded_string;
    std::cin >> encoded_string;
    std::cout << code(reversed_automaton, encoded_string) << std::endl;

    return 0;
}