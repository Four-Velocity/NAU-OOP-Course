#define _USE_MATH_DEFINES
#include <math.h>
#include <iostream>
class Figure {
public:
    virtual double area() {return 0.0;}
    virtual double perimeter() {return 0.0;}
};
class Rectangle : public Figure {
public:
    double ax, ay, bx, by, cx, cy, dx, dy, horizontal, vertical;
    Rectangle (double ax, double ay, double cx, double cy) {
        this->ax = ax;
        this->ay = ay;
        this->bx = ax;
        this->by = cy;
        this->cx = cx;
        this->cy = cy;
        this->dx = cx;
        this->dy = ay;
        this->horizontal = cx - ax;
        this->vertical = cy - ay;
    }
    double area() {
        return this->horizontal * this->vertical;
    }
    double perimeter() {
        return 2.0 * (this->vertical + this->horizontal);
    }
};
class Circle : public Figure {
public:
    double radius;
    Circle (double radius) { this->radius = radius;}
    double area() {
        return M_PI * pow(this->radius, 2.0);
    }
    double perimeter() {
        return 2.00 * M_PI * this->radius;
    }
};
int main() {
    std::cout << ("Так розташовані вугли прямокутника\nB--------C\n|        |\n|        |\nA--------D\n") << std::endl;
    double ax = 0.0, ay = 0.0, cx = 40.0, cy = 15.0;
    Rectangle rectangle(ax, ay, cx, cy);
    std::cout << "A(x) = " << ax <<"\nA(y) = " << ay << "\nC(x) = " << cx << "\nC(y) = " << cy << std::endl;
    std::cout << "Площа прямокутника = " << rectangle.area() << std::endl;
    std::cout << "Периметр прямокутника = " << rectangle.perimeter() << std::endl << std::endl;

    double radius = 18.00;
    Circle circle(radius);
    std::cout << "Площа кругу = " << circle.area() <<std::endl;
    std::cout << "Периметр кругу = " << circle.perimeter() <<std::endl;
    return 0;
}
