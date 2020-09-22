
int main(int argc, char *argv[]){
    int n = 10000000;
    map<int, int> nums;
    int start, finish, total = 0;
    int *test_sequence = new int[n];

    start = get_time();
    for (int i = 0; i < n; i++) {
        test_sequence[i] = rand_uns(-10000, 10000);
    }
    finish = get_time();
    total += finish - start;

    MinStack *mstack = new MinStack;

    start = get_time();
    for (int i  = 0; i < n; i++) {
        mstack->push(test_sequence[i]);
        if (nums.find(test_sequence[i]) != nums.end()) {
            nums[test_sequence[i]]++;
        } else{
            nums.insert({test_sequence[i], 1});
        }
        if (mstack->getMin() != nums.begin()->first) {
            cout << "NO";
            return 0;
        }
    }
    finish = get_time();
    total += finish - start;

    start = get_time();
    for (int i  = n - 1; i > 0; i--) {
        if (mstack->top() != test_sequence[i]) {
            cout << "NO";
            return 0;
        }
        mstack->pop();
        auto it = nums.find(test_sequence[i]);

        if (it->second == 1) {
            nums.erase(it);
        } else {
            it->second--;
        }

        if (mstack->getMin() != nums.begin()->first) {
            cout << "NO";
            return 0;
        }
    }
    finish  = get_time();
    total += finish - start;

    start = get_time();
    for (int i  = 0; i < n; i++) {
        if (n%2 == 0 && n >10) {
            mstack->push(test_sequence[i]);
            if (nums.find(test_sequence[i]) != nums.end()) {
                nums[test_sequence[i]]++;
            } else {
                nums.insert({test_sequence[i], 1});
            }
            if (mstack->getMin() != nums.begin()->first) {
                cout << "NO";
                return 0;
            }
        } else {
            int n = mstack->top();
            mstack->pop();
            auto it = nums.find(n);
            if (it->second == 1) {
                nums.erase(it);
            } else {
                it->second--;
            }
            if (mstack->getMin() != nums.begin()->first) {
                cout << "NO";
                return 0;
            }

        }
    }
    finish = get_time();
    total += finish - start;

    cout << "YES";
    delete[] test_sequence;
    return 0;
}
