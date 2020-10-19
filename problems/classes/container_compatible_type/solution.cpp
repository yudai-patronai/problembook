class TimeOfDay {
public:
    uint8_t hour, minute, second;
    
    TimeOfDay(uint8_t h, uint8_t m, uint8_t s) : hour(h), minute(m), second(s) {}
    
    bool IsAM() const {
        return IsValid() && (hour < 12);
    }
    
    bool IsPM() const {
        return IsValid() && (hour >= 12);
    }
    
    bool IsValid() const {
        return (hour < 24) && (minute < 60) && (second < 60);
    }
    
    bool operator<(const TimeOfDay& rhs) const {
        if (hour != rhs.hour) {
            return hour < rhs.hour;
        }
        if (minute != rhs.minute) {
            return minute < rhs.minute;
        }
        return second < rhs.second;
    }
    
    bool operator==(const TimeOfDay& rhs) const {
        return (hour == rhs.hour) && (minute == rhs.minute) && (second == rhs.second);
    }
}; 

template<>
struct std::hash<TimeOfDay> {
    size_t operator()(const TimeOfDay& t) const {
        return static_cast<size_t>(t.hour) * 3600ull + 
               static_cast<size_t>(t.minute) * 60ull + 
               static_cast<size_t>(t.second);
    }
};
