#include <iostream>
#include <cmath>
#include <stdexcept>
#include <fstream>

class Handler
{
private:
    double result;
public:
    double getResult() {
        if (isnan(result)) throw std::domain_error("NotImplementedError: Значення ще не обчислене");
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
    double * calculate(bool debug=false) {
        double first, second, third, fourth, fifth, sixth, seventh;
        static double ret[7];
        if (debug) std::cout << "\nПочаток обчислення" << std::endl;
        if (debug) std::cout << "[lg(4*" << b << "-" << c << ")*" << a << "]/[" << b << "+" << c << "/" << d << "-1] = ";
        first = 4 * b;
        ret[0] = first;
        if (debug) std::cout << "[lg(" << first << "-" << c << ")*" << a << "]/[" << b << "+" << c << "/" << d << "-1] = ";
        second = first - c;
        ret[1] = second;
        if (debug) std::cout << "[lg(" << second << ")*" << a << "]/[" << b << "+" << c << "/" << d << "-1] = ";
        if (second<=0) throw std::invalid_argument("ValueError: Базою логарифму не може бути <= 0");
        else {
            third = log10(second);
            ret[2] = third;
            if (debug) std::cout << "[" << third << "*" << a << "]/[" << b << "+" << c << "/" << d << "-1] = ";
        }
        fourth = third * a;
        ret[3] = fourth;
        if (debug) std::cout << "[" << fourth << "]/[" << b << "+" << c << "/" << d << "-1] = ";
        if (d==0) throw std::logic_error("ZeroDivisionError: d не може дорівнювати 0");
        else {
            fifth = c/d;
            ret[4] = fifth;
            if (debug) std::cout << "[" << fourth << "]/[" << b << "+" << fifth << "-1] = ";
        }
        sixth = b + fifth;
        ret[5] = sixth;
        if (debug) std::cout << "[" << fourth << "]/[" << sixth << "-1] = ";
        seventh = sixth - 1;
        ret[6] = seventh;
        if (debug) std::cout << "[" << fourth << "]/[" << seventh << "] = ";
        if (seventh==0) throw std::logic_error("ZeroDivisionError: b+c/d-1 не може дорівнювати 0");
        if (debug) std::cout << fourth / seventh << std::endl;
        this->result = fourth / seventh;
        return ret;
    }

    void logger(){
        std::ofstream log;
        double *calc;
        log.open("logs/c++.log.csv", std::ios_base::app);
        try {
            calc = calculate();
        }
        catch (const std::invalid_argument &e) {
            log << "eL";
        }
        catch (const std::logic_error &e) {
            log << "e0";
        }
        catch (const char *msg) {
            log << "e?";
        }
        try {
            log<<getResult()<< ", "<<calc[0]<<", "<<calc[1]<<", "<<calc[2]<<", "<<calc[3]<<", "<<calc[4]<<", "<<calc[5]<<", "<<calc[6]<<"\r\n";
        }
        catch (const std::domain_error &e) {
            log << "eI\r\n";
        }
        log.close();
    }
};

int main() {
    std::ifstream values;
    values.open("start_values.tsv");
    double a, b, c, d;
    std::ofstream log_f;
    log_f.open("logs/c++.log.csv", std::ios_base::out | std::ios_base::trunc);
    log_f << "Result,First,Second,Third,Fourth,Fifth,Sixth,Seventh\r\n";
    log_f.close();
    while (values >> a >> b >> c >> d){
        Handler handler(a, b, c, d);
        handler.logger();
    }
}
