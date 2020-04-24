#include <iostream>
#include <cmath>
#include <stdexcept>
#include <fstream>

using namespace std;

class Handler
{
private:
    double result;
public:
    double getResult() {
        if (isnan(result)) throw domain_error("NotImplementedError: Значення ще не обчислене");
        else return result;
    }
    double a, b, c, d;
    Handler(double a, double b, double c, double d) {
        this->a = a;
        this->b = b;
        this->c = c;
        this->d = d;
        this->result = nan("0");
    }
    void calculate() {
        double first, second, third, fourth, fifth, sixth, seventh;
        cout << "Початок обчислення" << endl;
        cout << "[lg(4*" << b << "-" << c << ")*" << a << "]/[" << b << "+" << c << "/" << d << "-1] = ";
        first = 4 * b;
        cout << "[lg(" << first << "-" << c << ")*" << a << "]/[" << b << "+" << c << "/" << d << "-1] = ";
        second = first - c;
        cout << "[lg(" << second << ")*" << a << "]/[" << b << "+" << c << "/" << d << "-1] = ";
        if (second<=0) throw invalid_argument("ValueError: Базою логарифму не може бути <= 0");
        else {
            third = log10(second);
            cout << "[" << third << "*" << a << "]/[" << b << "+" << c << "/" << d << "-1] = ";
        }
        fourth = third * a;
        cout << "[" << fourth << "]/[" << b << "+" << c << "/" << d << "-1] = ";
        if (d==0) throw logic_error("ZeroDivisionError: d не може дорівнювати 0");
        else {
            fifth = c/d;
            cout << "[" << fourth << "]/[" << b << "+" << fifth << "-1] = ";
        }
        sixth = b + fifth;
        cout << "[" << fourth << "]/[" << sixth << "-1] = ";
        seventh = sixth - 1;
        cout << "[" << fourth << "]/[" << seventh << "] = ";
        if (seventh==0) throw logic_error("ZeroDivisionError: b+c/d-1 не може дорівнювати 0");
        cout << fourth / seventh << endl;
        this->result = fourth / seventh;
    }

    void logger(bool rewrite = false){
        ofstream log;
        if (rewrite) log.open("c++.log.txt", ios_base::out | ios_base::trunc);
        else log.open("c++.log.txt", ios_base::app);
        if (log.is_open()) {
            try {
                calculate();
            }
            catch (const logic_error &e) {
                log << "e0";
            }
            catch (const invalid_argument &e) {
                log << "eL";
            }
            catch (const char *msg) {
                log << "e?";
            }
            try {
                log << getResult() << "\r\n";
            }
            catch (const domain_error &e) {
                log << "eI\r\n";
            }
            log.close();
        } else {
            throw runtime_error("Can't log!");
        }
    }
};
int main() {
    return 0;
}
