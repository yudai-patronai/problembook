---
id: f236f434-bc38-40a9-a36f-281128bd137c
longname: Одноступы
languages: [python]
tags: [class]
source_header: header.py
source_footer: footer.py
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Продолжая создавать остров одноступов вам необходимо реализовать абстрактный класс одноступа (`AbstractMonopod` - без реализации), в виде его потомков невидимого (`InvisibleMonopod`) и милого (`CuteMonopod`) одноступов.

Известно, что:
- абстрактный дракон умеет представляться (`get_hello_text`) и колдовать над числами (`make_magic`);
- при рождении (`__init__`) каждый одноступ запоминает своё имя в поле `name`;
- информация о виде (`invisible`, `cute`) являеться врождённой сразу для всех одноступов (классовый атрибут `status`);
- Невидимый одноступ Vasya возводит число в квадрат и представляеться `Hello, my name is Vasya. I'm Invisible squared monopod`;
- Милый одноступ Kostya умеет изменять знак числа на противоположный и представляеться `Hello, my name is Kostya. I'm Cute negative monopod`;
