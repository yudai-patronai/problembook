#include<iostream>
#include<cstdint>
#include<vector>
#include<unordered_set>


const char kFirstLetter = 'a';


bool vectors_prefix_equal(const std::vector<int32_t>& first, 
        const std::vector<int32_t>& second, int32_t prefix_len) {
    int32_t first_size = static_cast<int32_t>(first.size()),
            second_size = static_cast<int32_t>(second.size());
    if ((first_size < prefix_len || second_size < prefix_len) && first_size != second_size) {
        return false;
    }
    int32_t real_prefix_len = prefix_len < first_size ? prefix_len : first_size;
    for (int32_t i = 0; i < real_prefix_len; ++i) {
        if (first[i] != second[i]) {
            return false;
        }
    }
    return true;
}

void radix_sort_stable(std::vector<std::vector<int32_t>>& array, int32_t key_num) {
    int32_t digit_num = static_cast<int32_t>(array[0].size()),
            array_size = static_cast<int32_t>(array.size());

    std::vector<int32_t> buckets(key_num);
    std::vector<std::vector<int32_t>> temp_array(array_size);
    
    for (int32_t digit = digit_num - 1; digit >= 0; --digit) {
        for (int32_t i = 0; i < key_num; ++i) {
            buckets[i] = 0;
        }
        for (int32_t i = 0; i < array_size; ++i) {
            buckets[array[i][digit]] += 1;
        }
        std::vector<int32_t> cumulative_sum(key_num), used_counter(key_num);
        for (int32_t i = 1; i < key_num; ++i) {
            cumulative_sum[i] = cumulative_sum[i - 1] + buckets[i - 1];
        }
        for (int i = 0; i < array_size; ++i) {
            int32_t curr_position = cumulative_sum[array[i][digit]] + used_counter[array[i][digit]];
            used_counter[array[i][digit]] += 1;
            temp_array[curr_position].swap(array[i]);
        }
        array.swap(temp_array);
    }
}

int32_t prune_dfa(std::vector<std::vector<int32_t>>& transitions, 
        std::unordered_set<int32_t>& terminals, int32_t letter_num) {
    int32_t transitions_size = static_cast<int32_t>(transitions.size());
    std::vector<int32_t> stack(1);
    std::unordered_set<int32_t> reachable_states;
    reachable_states.insert(0);
    for (int32_t i = 0; i < static_cast<int32_t>(stack.size()); ++i) {
        for (auto end_state : transitions[stack[i]]) {
            if (reachable_states.find(end_state) == reachable_states.end()) {
                stack.push_back(end_state);
                reachable_states.insert(end_state);
            }
        }
    }
    int32_t last_reachable = transitions_size - 1;
    for (int32_t state = transitions_size - 1; state >= 0; --state) {
        if (reachable_states.find(state) == reachable_states.end()) {
            transitions[state].swap(transitions[last_reachable]);
            terminals.erase(state);
            if (terminals.find(last_reachable) != terminals.end()) {
                terminals.erase(last_reachable);
                terminals.insert(state);
            }
            for (int32_t i = 0; i < last_reachable; ++i) {
                for (int32_t j = 0; j < letter_num; ++j) {
                    if (transitions[i][j] == state) {
                        transitions[i][j] = last_reachable;
                    }
                    if (transitions[i][j] == last_reachable) {
                        transitions[i][j] = state;
                    }
                }
            }
            last_reachable -= 1;
        }
    }
    for (int32_t i = last_reachable + 1; i < transitions_size; ++i) {
        transitions.pop_back();
    }
    // return num of deleted states
    return transitions_size - static_cast<int>(transitions.size());
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int32_t state_num, end_num, letter_num;
    std::cin >> state_num >> end_num >> letter_num;

    std::unordered_set<int32_t> terminals;
    for (int i = 0; i < end_num; ++i) {
        int32_t end_node;
        std::cin >> end_node;
        terminals.insert(end_node);
    }

    std::vector<std::vector<int32_t>> transitions(state_num, std::vector<int32_t>(letter_num));
    for (int32_t i = 0; i < state_num; ++i) {
        for (int32_t j = 0; j < letter_num; ++j) {
            int32_t state_begin, state_end;
            char letter;
            std::cin >> state_begin >> letter >> state_end;
            transitions[state_begin][letter - kFirstLetter] = state_end;
        }
    }

    // pruning not needed as per statement
    // int32_t deleted_num = prune_dfa(transitions, terminals, letter_num);
    // state_num -= deleted_num;
    
    /* table for equivalence intersection:
     * row is state of dfa;
     * first letter_num columns are "letter equivalence", \delta(state, letter) ~ \delta(state_2, letter)
     * column #letter_num is state equivalence, state ~ state_2
     * last, #letter_num + 1 column, is index, table[i][-1] = i
     * it's either that or lots of vectors moving around
     */
    std::vector<std::vector<int32_t>> equivalence_table(
            state_num, std::vector<int>(letter_num + 2, 0)
    );
    const int32_t kStateEqvColumn = letter_num, kIndexColumn = letter_num + 1; 

    std::vector<int32_t> curr_partitions(state_num);
    for (auto end_state : terminals) {
        // partition init: terminal states in distinct partition
        curr_partitions[end_state] = 1;
    }

    std::vector<int32_t> prev_partitions;

    do {
        prev_partitions = curr_partitions;

        for (int32_t state = 0; state < state_num; ++state) {
            for (int32_t letter = 0; letter < letter_num; ++letter) {
                equivalence_table[state][letter] = curr_partitions[transitions[state][letter]];
            }
            equivalence_table[state][kIndexColumn] = state;
            equivalence_table[state][kStateEqvColumn] = prev_partitions[state];
        }

        int32_t key_num = state_num > 1 ? state_num : 2;
        radix_sort_stable(equivalence_table, key_num);

        int32_t temp_partition = equivalence_table[0][kIndexColumn];
        curr_partitions[equivalence_table[0][kIndexColumn]] = temp_partition;
        for (int32_t i = 1; i < state_num; ++i) {
            if (!vectors_prefix_equal(
                        equivalence_table[i - 1], 
                        equivalence_table[i], 
                        letter_num + 1)) {
                temp_partition = equivalence_table[i][kIndexColumn];
            }
            curr_partitions[equivalence_table[i][kIndexColumn]] = temp_partition;
        }   
    } while (!vectors_prefix_equal(prev_partitions, curr_partitions, state_num));
    auto answer = std::unordered_set<int32_t>(curr_partitions.begin(), curr_partitions.end()).size();
    std::cout << answer<< std::endl;
    return 0;
}
