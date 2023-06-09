---
id: e0514d4f-647c-4142-a15a-0749207de0dc
longname: Рейтинги браузеров
languages: [python]
tags: [varray, frequency, ege]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Результаты опроса по использованию браузеров представлены в виде списка с названиями платформы (`desktop` или `mobile`) и браузера. Количество голосов в исходном списке может быть велико (свыше 100000). Количество браузеров не превосходит 100.

Вам необходимо составить два рейтинга браузеров: по настольной платформе и по мобильной.

### Формат входных данных

На вход программе в первой строке подается количество ответов на опрос N. В каждой из последующих N строк записаны названия платформы (`desktop` или `mobile`) и браузера, которые предпочитает опрашиваемый. Длина строки не превосходит 100 символов, название браузера может содержать буквы, цифры пробелы и прочие символы.

### Формат выходных данных

Программа должна вывести два списка браузеров с указанием места в рейтинге. Каждый список начинается с заголовка `desktop browsers rating` или `mobile browsers rating`. Если по платформе голосов не было, то и её заголовок выводить не надо. Если браузеры получили одинаковое количество голосов, то необходимо указывать диапазон мест. Браузеры, делящие место в рейтинге необходимо выводить в том порядке, в котором они были в опросе для соответствующей платформы.

Подробнее о формате вывода посмотрите в примерах.

### Примеры

```
-> 6
-> desktop Netscape Navigator
-> desktop Opera
-> desktop Google Chrome
-> mobile Opera
-> desktop Google Chrome
-> mobile Google Chrome
--
<- desktop browsers rating
<- 1 Google Chrome
<- 2 - 3 Netscape Navigator
<- 2 - 3 Opera
<- mobile browsers rating
<- 1 - 2 Opera
<- 1 - 2 Google Chrome
```
