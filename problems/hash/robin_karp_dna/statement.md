---
id: 04aad064-b0fd-41ea-9f09-4827e3e5f2c2
longname: Robin-Karp-Dna
languages: [cpp]
tags: [easy, hash]
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---
Молекула ДНК состоит из серии нуклеотидов обозначеных буквами A, C, G, T. Например, "ACGAATTCCG".
Изучая послеовательность ДНК часто вычленяют повторяющиеся цепочки различной длинны.
Задача - написать функцию, которая находит все 10 буквенные последовательности, которые встречаются более 1 раза
в заданной молекуле;


### Формат входных данных

Строка состоящая из заглавных букв A, C, G, T.

### Формат выходных данных

Вывести все подстроки которые встретились более одного раза;
Подстроки должны выводится в том порядке, в котором они следуют в строке.

```
// Ваша функция
vector<string> findRepDna(string s) {....}

int main() {
    std::vector<std::string> dna_substr;
    std::string dna_str;
    getline(std::cin, dna_str);
    dna_substr = findRepDna(dna_str);
    for (int i = 0; i < dna_substr.size(); i++) {
        std:: cout << dna_substr[i] <<" ";
    }
    return 0;
}
```

### Примеры

```
-> "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
--
<- ["AAAAACCCCC","CCCCCAAAAA"]
```

