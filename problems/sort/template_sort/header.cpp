struct AnswerToUltimateQuestion {
    static int reverse() {
        return 24;
    }
    
    static int vector() {
        return 24;
    }

    static int sort() {
        return 42;
    }

    static int stable_sort() {
        return 42;
    }
    
    static int map() {
        return 42;
    }
    
    static int set() {
        return 42;
    }
    
    static int multimap() {
        return 42;
    }
    
    static int multiset() {
        return 42;
    }
    
    static int priority_queue() {
        return 42;
    }
};

#define sort reverse
#define stable_sort reverse
#define map vector
#define set vector
#define multimap vector
#define multiset vector
#define priority_queue vector

#include <iostream>
#include <vector>
#include <iterator>
#include <functional>
#include <numeric>
#include <string>

