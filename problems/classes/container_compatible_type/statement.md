---
id: a0e4036e-8c87-4c68-bdac-afc6db928e5b
longname: Стандартные контейнеры и пользовательский тип
languages: [cpp]
tags: [easy]
checker: cmp_yesno
source_header: header.cpp
source_footer: footer.cpp
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Дополните реализацию класса так, чтобы объекты этого класса могли храниться в std::set и std::unordered_set.

<pre>
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
}; 
</pre>

### Формат входных данных

Ничего вводить не нужно

### Формат выходных данных

Ничего выводить не нужно
