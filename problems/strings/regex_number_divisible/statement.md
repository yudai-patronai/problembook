---
id: 1d431103-7bd1-445b-a640-b7c58d77fb70
longname: Регулярное выражение для проверки кратности
languages: [cpp]
tags: [strings, regex]
checker: cmp_file
source_header: header.cpp
source_footer: footer.cpp
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Напишите регулярное выражение, которое по строке, представляющей собой неотрицательное целое число в двоичной системе счисления без ведущих нулей, проверяет, делится ли это число на 5. От вас ожидается всего одна функция, которая должна возвращать строку:

<pre>
std::string GetRegex() {/* ваш код */}
</pre>

Для локального тестирования можно использовать следующую функцию main (функция на сервере проверки аналогична):

<pre>
int main() {
    std::string div5reg = GetRegex();
    std::regex div5(div5reg, std::regex_constants::nosubs | std::regex_constants::ECMAScript);
    if(!std::regex_match("1111", div5)) { // 1111bin = 15dec
        std::cout << "Test failed\n";
    }
    } else {
        std::cout << "Test passed\n";
    }
}
</pre>

Справочный материал по синтаксису регулярных выражений: http://www.cplusplus.com/reference/regex/ECMAScript/
