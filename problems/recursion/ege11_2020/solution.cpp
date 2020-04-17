#include <iostream>

int64_t S(int k) {
        int64_t res = k;
        if (k > 2)
        {
                res = k + S(k - 1) + S(k / 2);
        }
        return res;
}


int main() {
	int32_t n;
	std::cin >> n;
        std::cout << S(n) << std::endl;
        return 0;
}

