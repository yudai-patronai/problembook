
#include <vector>
#include <unordered_set>
#include <stdexcept>
#include <iostream>
#include <type_traits>

struct Call {
    handle_t handle;
    std::string arg;
    
    Call(handle_t h, const std::string& s)
    : handle(h), arg(s) {}
};

class TestSet {
private:
    std::vector<Call> expected_calls;
    size_t call_number;
    bool has_errors;
    std::unordered_set<handle_t> open_handles;
        
    TestSet(const std::vector<Call>& expected) {
        Reset(expected);
    }
    
    TestSet() = default;
public:
    TestSet(const TestSet&) = delete;
    TestSet(TestSet&&) = delete;
    TestSet& operator=(const TestSet&) = delete;
    TestSet& operator=(TestSet&&) = delete;
    
    void Reset(const std::vector<Call>& expected) {
        expected_calls = expected;
        call_number = 0;
        has_errors = false;
        
        open_handles.clear();
        for (const auto& call: expected) {
            open_handles.insert(call.handle);
        }
    }
    
    static TestSet& GetInstance() {
        static TestSet instance;
        return instance;
    }
    
    void CheckWriteCall(handle_t handle, const std::string& arg) {
        if (
            (call_number >= expected_calls.size()) || 
            (expected_calls[call_number].handle != handle) || 
            (expected_calls[call_number].arg != arg) ||
            (open_handles.find(handle) == open_handles.end())
           ) 
        {
            has_errors = true;
        }
        
        ++call_number;
        return;
    }
   
    void CheckCloseCall(handle_t handle) {
        if (open_handles.find(handle) != open_handles.end()) {
            open_handles.erase(handle);
        } else {
            has_errors = true;
        }
    }
        
    bool GetResult() const {
        return 
            open_handles.empty() && 
            (call_number == expected_calls.size()) && 
            !has_errors;
    }
};

void raw_write(handle_t handle, const std::string& content) {
    TestSet::GetInstance().CheckWriteCall(handle, content);
}
void raw_close(handle_t handle) {
    TestSet::GetInstance().CheckCloseCall(handle);
}

int main() {
    std::vector<std::string> samples {
        "Never gonna give you up",
        "Never gonna let you down",
        "Never gonna run around and desert you",
        "Never gonna make you cry",
        "Never gonna say goodbye",
        "Never gonna tell a lie and hurt you"
    };
    
    // 1. Simple test case
    TestSet::GetInstance().Reset({
        {1, samples[0]},
        {2, samples[1]},
        {3, samples[2]},
        {2, samples[3]},
        {4, samples[4]},
        {1, samples[5]},
    });
    
    {
        IOWrapper io1(1), io2(2), io3(3), io4(4);

        io1.Write(samples[0]);
        io2.Write(samples[1]);
        io3.Write(samples[2]);
        io2.Write(samples[3]);
        io4.Write(samples[4]);
        io1.Write(samples[5]);
    }
    
    if (!TestSet::GetInstance().GetResult()) {
        std::cout << "NO\n";
        return 1;
    }
    
    // 2. Check if move constructor and assignment work
    TestSet::GetInstance().Reset({
        {1, samples[0]},
        {2, samples[1]},
        {1, samples[2]},
        {2, samples[3]},
    });
    
    {
        IOWrapper io1(1), io2(2);
        io1.Write(samples[0]);
        
        IOWrapper io1_new(std::move(io1));
        io1 = std::move(io2);
        
        io1.Write(samples[1]); // handle=2 !
        io1_new.Write(samples[2]);
        
        io2 = std::move(io1);
        io2.Write(samples[3]);
    }
    if (!TestSet::GetInstance().GetResult()) {
        std::cout << "NO\n";
        return 1;
    }
    
    // 3. Extra rules, extra tests
    if (
        std::is_default_constructible<IOWrapper>::value ||
        std::is_copy_constructible<IOWrapper>::value
    ) {
        std::cout << "NO\n";
        return 1;
    }
    
    std::cout << "YES\n";
    return 0;
} 
