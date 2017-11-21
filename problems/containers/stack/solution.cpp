#include <iostream>
#include <stack>

int main() {
    std::stack<int> st;

    int n;

    do {
        std::cin >> n;
        if (n == 0)
            break;

        if (n > 0) {
            st.push(n);
        } else if (!st.empty()) {
            if (-n >= st.top()) {
                st.pop();
            } else {
                st.top() += n;
            }
        }
    } while (true);

    std::cout << st.size() << " " << (st.empty() ? -1 : st.top()) << std::endl;

    return 0;
}
