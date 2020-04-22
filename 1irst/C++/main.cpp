#include <iostream>
using std::string;

class BaseString {
protected:
    string value;
public:
    BaseString(string v){this->value = v;}
    int len() {
        int result = 0;
        for(int i=0;this->value[i]!='\0';++i) {
            ++result;
        }
        return result;
    }
    string get() {
        return value;
    }
};

class SymbolString : public BaseString
{
public:
    SymbolString(string v) : BaseString(v) {};
    string replace(char a, char b) {
        string result = this->value;
        for(int i=0;i< this->len();++i) {
            if (result[i] == a) {
                string a1 = result.substr(0,i);
                string a2;
                a2.push_back(b);
                string a3 = result.substr(i+1);
                result = a1 + a2 + a3;
            }
        }
        return result;
    }
};

int main() {
    BaseString baseS("Foo Bar");
    SymbolString symbolS("Spam Eggs");
    std::cout << "Довжина базового рядка: " << baseS.len() << std::endl;
    std::cout << "Довжина символьного рядка: " << symbolS.len() << std::endl;
    std::cout << "Замінемо 'g' на 'b' у символьному рядку" << std::endl;
    std::cout << "Результат: " << symbolS.replace('g', 'b') << std::endl;
    return 0;
}
