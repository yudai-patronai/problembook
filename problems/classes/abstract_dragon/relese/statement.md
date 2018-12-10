---
id: 4562ef8b-6fcb-4301-ba5f-1f9d0b385bac
longname: Абстрактный Дракон
languages: [python]
tags: [class]
source_header: header.py
source_footer: footer.py
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Вам необходимо реализовать абстрактный класс математического дракона (`AbstractDragon`), 
в виде его потомков `GreenDragon` и `BlueDragon`.

Известно, что:
- абстрактный дракон умеет представляться (`get_intro_text`) и производить математическое действие (`make_action`);
- при рождении (`__init__`) каждый дракон запоминает своё имя в поле `name`;
- информация о цвете (`Green`, `Blue`) являеться врождённой сразу для всех драконов (классовый атрибут `color`);
- Зелёный дракон Vasya возводит число в квадрат и представляеться `Hello, my name is Vasya. I'm Green squared dragon`;
- Синий дракон Kostya умеет изменять знак числа на противоположный и представляеться `Hello, my name is Kostya. I'm Blue negative dragon`;
