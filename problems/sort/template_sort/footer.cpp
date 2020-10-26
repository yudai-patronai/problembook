
namespace checker {
static bool isOK = true;

template <class TFwdIter, class TCmp = std::less<typename std::iterator_traits<TFwdIter>::value_type>>
bool IsSorted(TFwdIter begin, TFwdIter end, TCmp cmp = {}) {
    if (begin == end) {
        return true;
    }

    auto next = begin;
    while (++next != end) {
        if (cmp(*next, *begin)) {
            return false;
        }
        begin = next;
    }
    return true;
}

template <class T, class TEq = std::equal_to<T>>
bool VectorsEq(const std::vector<T>& lhs, const std::vector<T>& rhs, TEq eq = {}) {
    if (lhs.size() != rhs.size()) {
        return false;
    }

    for (size_t i = 0; i < lhs.size(); ++i) {
        if (!eq(lhs[i], rhs[i])) {
            return false;
        }
    }
    return true;
}

void Require(bool val, const std::string& what, const std::string& fn, const int line) {
    if (!val) {
        isOK = false;
        std::cout << fn << ":" << line << "\t|\tCheck failed: " << what << "\n";
    }
}

class Int {
public:
    Int(int i) : value(i) {}

    bool IsLess(const Int& rhs) const {
        return value < rhs.value;
    }

    bool IsEqual(const Int& rhs) const {
        return value == rhs.value;
    }

private:
    // Hide operators
    bool operator<(const Int& rhs) const {
        return value < rhs.value;
    }

    bool operator==(const Int& rhs) const {
        return value == rhs.value;
    }

    int value;
};

class FriendlyInt {
public:
    FriendlyInt(int i) : value(i) {}
private:
    friend class std::less<FriendlyInt>;
    friend class std::equal_to<FriendlyInt>;

    // Hide operators
    bool operator<(const FriendlyInt& rhs) const {
        return value < rhs.value;
    }

    bool operator==(const FriendlyInt& rhs) const {
        return value == rhs.value;
    }

    int value;
};

}  // namespace checker

#define REQUIRE(expr) checker::Require((expr), #expr, __FILE__, __LINE__);

int main() {
    int n;
    std::cin >> n;
    
    if (n == 0) {
        std::vector<int> a{6, 1, 3, 2, 5, 4};
        Sort(a.begin(), a.end());
        REQUIRE(checker::VectorsEq(a, {1, 2, 3, 4, 5, 6}))
    }

    if (n == 1) {
        std::vector<int> a{6, 1, 3, 2, 5, 4};
        Sort(&a);
        REQUIRE(checker::VectorsEq(a, {1, 2, 3, 4, 5, 6}))
    }
    
    if (n == 2) {
        std::vector<int> a{6, 1, 3, 2, 5, 4};
        Sort(a.begin(), a.end(), std::greater<int>());
        REQUIRE(checker::VectorsEq(a, {6,5,4,3,2,1}))
    }

    if (n > 2) {
        {
            int* a = new int[6]{6, 1, 3, 2, 5, 4};

            Sort(a, a + 6);
            REQUIRE(a[0] == 1)
            REQUIRE(a[1] == 2)
            REQUIRE(a[2] == 3)
            REQUIRE(a[3] == 4)
            REQUIRE(a[4] == 5)
            REQUIRE(a[5] == 6)
        }

        {
            std::vector<checker::Int> a{{6}, {1}, {3}, {2}, {5}, {4}};
            Sort(a.begin(), a.end(),
                [](const checker::Int& lhs, const checker::Int& rhs) { return lhs.IsLess(rhs); });

            REQUIRE(
                checker::VectorsEq(
                    a, {{1},{2},{3},{4},{5},{6}},
                    [](const checker::Int& lhs, const checker::Int& rhs) { return lhs.IsEqual(rhs); }
                )
            )
        }

        {
            std::vector<checker::FriendlyInt> a{{6}, {1}, {3}, {2}, {5}, {4}};
            Sort(a.begin(), a.end());

            REQUIRE(checker::VectorsEq(a, {{1},{2},{3},{4},{5},{6}}))
        }

        {
            if (AnswerToUltimateQuestion::sort() + 
                AnswerToUltimateQuestion::stable_sort() +
                AnswerToUltimateQuestion::map() +
                AnswerToUltimateQuestion::set() +
                AnswerToUltimateQuestion::multimap() +
                AnswerToUltimateQuestion::multiset() +
                AnswerToUltimateQuestion::priority_queue()
                != 168) {
                bool violation_detected = true;
                REQUIRE(!violation_detected)
            }
        }

        {
            std::vector<uint64_t> a;
            a.reserve(100000);

            for (size_t i = 10000; i > 0; --i) {
                for (size_t j = 0; j < 10; ++j) {
                    a.push_back(i * 10 + j);
                }
            }

            Sort(&a);

            REQUIRE(checker::IsSorted(a.begin(), a.end()));
        }
        
        {
            std::cin >> n;
            std::vector<int8_t> v(n);
            
            for (auto i = 0; i < n; ++i) {
                std::cin >> v[i];
            }
            std::cout << "Token: " << std::hex << Integrity::generate(&v[0], n) << "\n";
        }
    }

    if (checker::isOK) {
        std::cout << "All checks passed\n";
    }
}

