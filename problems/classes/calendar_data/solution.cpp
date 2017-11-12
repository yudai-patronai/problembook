#include <iostream>

class CalendarData {
 public:
     CalendarData(const int& new_day, const int& new_month,
     const int& new_year) {
         day = new_day;
         month = new_month;
         year = new_year;
     }
     ~CalendarData() {
         std::cout << day << "." << month << "." << year << std::endl;
     }
 private:
     int day;
     int month;
     int year;
};
