#include <string>
#include <iostream>
#include <vector>

typedef struct MyStruct {
    int number;
    std::string word;
} simpleStruct;

class MyClass {
 public:
     void AddElement(const int& new_number, const std::string& new_word) {
         simpleStruct new_struct = { new_number, new_word };
         int size = static_cast<int>(myStructInfo.size());
         for (int i = 0; i < size; ++i) {
             if (myStructInfo[i].number == new_number &&
                 myStructInfo[i].word == new_word)
                 return;
         }
         myStructInfo.push_back(new_struct);
     }
     void PrintStructures() {
        int size = static_cast<int>(myStructInfo.size());
         for (int i = 0; i < size; ++i) {
             std::cout << myStructInfo[i].number <<
             " " << myStructInfo[i].word << std::endl;
         }
     }
 private:
     std::vector<simpleStruct> myStructInfo;
};
